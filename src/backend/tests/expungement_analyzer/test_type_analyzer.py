import unittest

from datetime import datetime, timedelta
from expungeservice.expungement_analyzer.type_analyzer import TypeAnalyzer
from expungeservice.crawler.models.charge import Charge
from expungeservice.crawler.models.charge import Disposition


class TestSingleChargeConvictions(unittest.TestCase):

    def setUp(self):
        self.type_analyzer = TypeAnalyzer()
        one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%m/%d/%Y')
        last_week = (datetime.today() - timedelta(days=7)).strftime('%m/%d/%Y')
        self.single_charge = {'name': '', 'statute': '', 'level': '', 'date': one_month_ago}
        disposition = {'ruling': 'Convicted', 'date': last_week}
        self.convicted_disposition = Disposition(**disposition)
        self.charges = []

    def create_charge(self):
        charge = Charge(**self.single_charge)
        charge.disposition = self.convicted_disposition
        return charge

    def test_felony_class_a_charge(self):
        self.single_charge['name'] = 'Assault in the first degree'
        self.single_charge['statute'] = '163.185'
        self.single_charge['level'] = 'Felony Class A'
        felony_class_a = self.create_charge()
        self.charges.append(felony_class_a)
        self.type_analyzer.evaluate(self.charges)

        assert felony_class_a.type_analysis.eligibility is False
        assert felony_class_a.type_analysis.reason == 'Ineligible under 137.225(5)'
