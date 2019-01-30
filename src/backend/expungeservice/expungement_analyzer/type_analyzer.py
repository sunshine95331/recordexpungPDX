class TypeAnalyzer:

    def evaluate(self, charges):
        if charges[0].disposition.ruling == 'Dismissed' or charges[0].disposition.ruling == 'Acquitted' or charges[0].disposition.ruling == 'No Complaint':
            charges[0].expungement_result.set_type_eligibility(True)
            charges[0].expungement_result.set_reason('Eligible under 137.225(1)(b)')

        elif TypeAnalyzer.__marijuana_ineligible(charges):
            charges[0].expungement_result.set_type_eligibility(False)
            charges[0].expungement_result.set_reason('Ineligible under 137.226')

        elif TypeAnalyzer.__list_b_charge(charges[0]):
            charges[0].expungement_result.set_reason('Further Analysis Needed')

        elif TypeAnalyzer.__ineligible_under_137_225_5(charges[0]):
            charges[0].expungement_result.set_type_eligibility(False)
            charges[0].expungement_result.set_reason('Ineligible under 137.225(5)')

        elif charges[0].level == 'Felony Class C' or charges[0].level == 'Misdemeanor Class C':
            charges[0].expungement_result.set_type_eligibility(True)
            charges[0].expungement_result.set_reason('Eligible under 137.225(5)(b)')

    @staticmethod
    def __ineligible_under_137_225_5(charge):
        return TypeAnalyzer.__crime_against_person(charge) or TypeAnalyzer.__traffic_crime(charge) or TypeAnalyzer.__felony_class_a(charge)

    @staticmethod
    def __crime_against_person(charge):
        statute = int(charge.statute[0:6])
        statute_ranges = (range(163305, 163480), range(163670, 163694), range(167008, 167108), range(167057, 167081))
        return any(statute in statute_range for statute_range in statute_ranges)

    @staticmethod
    def __traffic_crime(charge):
        statute = int(charge.statute[0:3])
        statute_range = range(801, 826)
        return statute in statute_range

    @staticmethod
    def __felony_class_a(charge):
        return charge.level == 'Felony Class A'

    @staticmethod
    def __marijuana_ineligible(charges):
        if charges[0].statute == '475B3493C':
            return True
        else:
            ineligible_statutes = ['475B359', '475B367', '475B371', '167262']
            return charges[0].statute[0:7] in ineligible_statutes

    @staticmethod
    def __list_b_charge(charge):
        ineligible_statutes = ['163200', '163205', '163575', '163535', '163175', '163275', '162165', '163525', '164405', '164395', '162185', '166220', '163225', '163165']
        return charge.statute[0:6] in ineligible_statutes
