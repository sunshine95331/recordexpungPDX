from datetime import date
from dateutil.relativedelta import relativedelta


class TimeAnalyzer:

    THREE_YEARS = 3
    TEN_YEARS = 10

    def __init__(self, most_recent_conviction=None, second_most_recent_conviction=None, most_recent_dismissal=None):
        """

        :param most_recent_conviction: Most recent conviction if one exists from within the last ten years
        :param second_most_recent_conviction: Second most recent conviction if one exists from within the last ten years
        :param most_recent_dismissal: Most recent dismissal if one exists from within the last three years
        """
        self._most_recent_conviction = most_recent_conviction
        self._second_most_recent_conviction = second_most_recent_conviction
        self._most_recent_dismissal = most_recent_dismissal

    def evaluate(self, charges):
        if self._most_recent_conviction:
            self._mark_all_charges_ineligible(charges)
            if self._most_recent_conviction_is_greater_than_three_years_old():
                self._mark_most_recent_conviction_eligible()
            elif self._second_most_recent_conviction:
                self._mark_mrc_ineligible('Multiple convictions within last ten years', self.TEN_YEARS)
            else:
                self._mark_mrc_ineligible('Most recent conviction is less than three years old', self.THREE_YEARS)
        elif self._most_recent_dismissal:
            pass
        else:
            TimeAnalyzer._mark_all_eligible(charges)

    def _most_recent_conviction_is_greater_than_three_years_old(self):
        three_years_ago = date.today() + relativedelta(years=-3)
        return self._most_recent_conviction.disposition.date <= three_years_ago

    def _mark_all_charges_ineligible(self, charges):
        for charge in charges:
            self._mark_ineligible(charge, 'Time-ineligible under 137.225(7)(b)', self.TEN_YEARS)

    def _mark_ineligible(self, charge, reason, years):
        TimeAnalyzer._mark_eligibleness(charge, False)
        TimeAnalyzer._ineligible_reason(charge, reason)
        TimeAnalyzer._date_of_eligibility(charge, self._most_recent_conviction, years)

    def _mark_most_recent_conviction_eligible(self):
        self._most_recent_conviction.expungement_result.time_eligibility = True
        self._most_recent_conviction.expungement_result.time_eligibility_reason = ''
        self._most_recent_conviction.expungement_result.date_of_eligibility = None

    def _mark_mrc_ineligible(self, reason, years):
        TimeAnalyzer._mark_eligibleness(self._most_recent_conviction, False)
        TimeAnalyzer._ineligible_reason(self._most_recent_conviction, reason)
        if self._second_most_recent_conviction:
            TimeAnalyzer._date_of_eligibility(self._most_recent_conviction, self._second_most_recent_conviction, years)
        else:
            TimeAnalyzer._date_of_eligibility(self._most_recent_conviction, self._most_recent_conviction, years)

    @staticmethod
    def _three_years_from_disposition(charge):
        return charge.disposition.date + relativedelta(years=+3)

    @staticmethod
    def _mark_eligibleness(charge, eligibility):
        charge.expungement_result.time_eligibility = eligibility

    @staticmethod
    def _ineligible_reason(charge, reason):
        charge.expungement_result.time_eligibility_reason = reason

    @staticmethod
    def _date_of_eligibility(charge, mrc, years):
        charge.expungement_result.date_of_eligibility = mrc.disposition.date + relativedelta(years=years)

    @staticmethod
    def _mark_all_eligible(charges):
        for charge in charges:
            TimeAnalyzer._mark_eligibleness(charge, True)
