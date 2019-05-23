import unittest

from expungeservice.models.case import Case
from tests.factories.case_factory import CaseFactory


class TestCaseBalanceDue(unittest.TestCase):

    def setUp(self):
        self.case = Case(("John Doe", "1990"), "", "", ("1/1/2019",""), ("",""), "", "")

    def test_balance_due_getter_setter(self):     

        self.case.set_balance_due("123.45")
        assert self.case.get_balance_due() == 123.45

        self.case.set_balance_due("2,345.67")
        assert self.case.get_balance_due() == 2345.67
        
        self.case.set_balance_due(12345.67)
        assert self.case.get_balance_due() == 12345.67

        self.case.set_balance_due("0")
        assert self.case.get_balance_due() == 0  


class TestCaseClosedMethod(unittest.TestCase):

    def setUp(self):
        self.case = CaseFactory.create()

    def test_it_returns_true_for_a_closed_case(self):
        self.case.current_status = 'Closed'
        assert self.case.closed() is True

    def test_it_returns_false_for_an_open_case(self):
        self.case.current_status = 'Open'
        assert self.case.closed() is False

    def test_it_returns_true_for_an_inactive_case(self):
        self.case.current_status = 'Inactive'
        assert self.case.closed() is True
