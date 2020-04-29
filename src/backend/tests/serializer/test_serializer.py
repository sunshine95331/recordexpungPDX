import pytest

from expungeservice.expunger import Expunger
from expungeservice.serializer import ExpungeModelEncoder

from tests.test_crawler_expunger import (
    record_with_open_case,
    empty_record,
    partial_dispos_record,
    record_without_dispos,
    record_with_various_categories,
    record_with_specific_dates,
)

import json


@pytest.fixture(
    params=[
        pytest.lazy_fixture("record_with_open_case"),
        pytest.lazy_fixture("empty_record"),
        pytest.lazy_fixture("partial_dispos_record"),
        pytest.lazy_fixture("record_without_dispos"),
        pytest.lazy_fixture("record_with_various_categories"),
        pytest.lazy_fixture("record_with_specific_dates"),
    ]
)
def _record(request):
    return request.param


def test_round_trip_various_records(_record):
    json.loads(json.dumps(_record, cls=ExpungeModelEncoder))


def test_record_with_various_categories(record_with_various_categories):
    record_dump = """
{
  "total_balance_due": 4550.4,
  "cases": [
    {
      "name": "Doe, John D",
      "birth_year": 1943,
      "case_number": "X0003",
      "citation_number": "",
      "location": "Multnomah",
      "date": "Apr 1, 2012",
      "violation_type": "Offense Misdemeanor",
      "current_status": "Closed",
      "balance_due": 1516.8,
      "probation_revoked": null,
      "case_detail_link": "https://publicaccess.courts.oregon.gov/PublicAccessLogin/CaseDetail.aspx?CaseID=X0003",
      "charges": [
        {
          "id": "X0003-1-0",
          "name": "Driving Uninsured",
          "statute": "806010",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "No Complaint",
            "status": "No Complaint",
            "amended": false
          },
          "ambiguous_charge_id": "X0003-1",
          "case_number": "X0003",
          "expungement_result": {
            "type_eligibility": {
              "status": "Eligible",
              "reason": "Dismissals are generally eligible under 137.225(1)(b)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Ten years from most recent conviction (137.225(7)(b))",
              "date_will_be_eligible": "Jun 12, 2027"
            },
            "charge_eligibility": {
              "status": "Will be eligible",
              "label": "Eligible Jun 12, 2027"
            }
          },
          "type_name": "Dismissed Criminal Charge",
          "expungement_rules": "All non-duii criminal charges that are dismissed fall under this charge type."
        },
        {
          "id": "X0003-2-0",
          "name": "Violation Driving While Suspended or Revoked",
          "statute": "811175",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Dismissed",
            "status": "Dismissed",
            "amended": false
          },
          "ambiguous_charge_id": "X0003-2",
          "case_number": "X0003",
          "expungement_result": {
            "type_eligibility": {
              "status": "Eligible",
              "reason": "Dismissals are generally eligible under 137.225(1)(b)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Ten years from most recent conviction (137.225(7)(b))",
              "date_will_be_eligible": "Jun 12, 2027"
            },
            "charge_eligibility": {
              "status": "Will be eligible",
              "label": "Eligible Jun 12, 2027"
            }
          },
          "type_name": "Dismissed Criminal Charge",
          "expungement_rules": "All non-duii criminal charges that are dismissed fall under this charge type."
        },
        {
          "id": "X0003-3-0",
          "name": "Failure to Obey Traffic Control Device",
          "statute": "811265",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Convicted",
            "status": "Convicted",
            "amended": false
          },
          "ambiguous_charge_id": "X0003-3",
          "case_number": "X0003",
          "expungement_result": {
            "type_eligibility": {
              "status": "Ineligible",
              "reason": "Ineligible under 137.225(7)(a)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Never. Type ineligible charges are always time ineligible.",
              "date_will_be_eligible": "Dec 31, 9999"
            },
            "charge_eligibility": {
              "status": "Ineligible",
              "label": "Ineligible"
            }
          },
          "type_name": "Traffic Offense",
          "expungement_rules": "A conviction for a State or municipal traffic offense is not eligible for expungement. Common convictions under this category include Driving While Suspended/Revoked, Possession of a Stolen Vehicle, Driving Under the Influence of Intoxicants, and Failure to Perform Duties of a Driver."
        }
      ]
    },
    {
      "name": "Doe, John D",
      "birth_year": 1943,
      "case_number": "X0002",
      "citation_number": "C0002",
      "location": "Multnomah",
      "date": "Apr 11, 1963",
      "violation_type": "Offense Felony",
      "current_status": "Closed",
      "balance_due": 1516.8,
      "probation_revoked": null,
      "case_detail_link": "https://publicaccess.courts.oregon.gov/PublicAccessLogin/CaseDetail.aspx?CaseID=X0002",
      "charges": [
        {
          "id": "X0002-1-0",
          "name": "Driving Uninsured",
          "statute": "806010",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Dismissed",
            "status": "Dismissed",
            "amended": false
          },
          "ambiguous_charge_id": "X0002-1",
          "case_number": "X0002",
          "expungement_result": {
            "type_eligibility": {
              "status": "Eligible",
              "reason": "Dismissals are generally eligible under 137.225(1)(b)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Ten years from most recent conviction (137.225(7)(b))",
              "date_will_be_eligible": "Jun 12, 2027"
            },
            "charge_eligibility": {
              "status": "Will be eligible",
              "label": "Eligible Jun 12, 2027"
            }
          },
          "type_name": "Dismissed Criminal Charge",
          "expungement_rules": "All non-duii criminal charges that are dismissed fall under this charge type."
        },
        {
          "id": "X0002-2-0",
          "name": "Violation Driving While Suspended or Revoked",
          "statute": "811175",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Convicted",
            "status": "Convicted",
            "amended": false
          },
          "ambiguous_charge_id": "X0002-2",
          "case_number": "X0002",
          "expungement_result": {
            "type_eligibility": {
              "status": "Ineligible",
              "reason": "Ineligible under 137.225(7)(a)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Never. Type ineligible charges are always time ineligible.",
              "date_will_be_eligible": "Dec 31, 9999"
            },
            "charge_eligibility": {
              "status": "Ineligible",
              "label": "Ineligible"
            }
          },
          "type_name": "Traffic Offense",
          "expungement_rules": "A conviction for a State or municipal traffic offense is not eligible for expungement. Common convictions under this category include Driving While Suspended/Revoked, Possession of a Stolen Vehicle, Driving Under the Influence of Intoxicants, and Failure to Perform Duties of a Driver."
        },
        {
          "id": "X0002-3-0",
          "name": "Failure to Obey Traffic Control Device",
          "statute": "811265",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Convicted",
            "status": "Convicted",
            "amended": false
          },
          "ambiguous_charge_id": "X0002-3",
          "case_number": "X0002",
          "expungement_result": {
            "type_eligibility": {
              "status": "Ineligible",
              "reason": "Ineligible under 137.225(7)(a)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Never. Type ineligible charges are always time ineligible.",
              "date_will_be_eligible": "Dec 31, 9999"
            },
            "charge_eligibility": {
              "status": "Ineligible",
              "label": "Ineligible"
            }
          },
          "type_name": "Traffic Offense",
          "expungement_rules": "A conviction for a State or municipal traffic offense is not eligible for expungement. Common convictions under this category include Driving While Suspended/Revoked, Possession of a Stolen Vehicle, Driving Under the Influence of Intoxicants, and Failure to Perform Duties of a Driver."
        }
      ]
    },
    {
      "name": "Doe, John D",
      "birth_year": 1943,
      "case_number": "X0001",
      "citation_number": "C0001",
      "location": "Multnomah",
      "date": "Mar 23, 1963",
      "violation_type": "Offense Misdemeanor",
      "current_status": "Closed",
      "balance_due": 1516.8,
      "probation_revoked": null,
      "case_detail_link": "https://publicaccess.courts.oregon.gov/PublicAccessLogin/CaseDetail.aspx?CaseID=X0001",
      "charges": [
        {
          "id": "X0001-1-0",
          "name": "Driving Uninsured",
          "statute": "806010",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Convicted - Failure to show",
            "status": "Convicted",
            "amended": false
          },
          "ambiguous_charge_id": "X0001-1",
          "case_number": "X0001",
          "expungement_result": {
            "type_eligibility": {
              "status": "Ineligible",
              "reason": "Ineligible under 137.225(7)(a)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Never. Type ineligible charges are always time ineligible.",
              "date_will_be_eligible": "Dec 31, 9999"
            },
            "charge_eligibility": {
              "status": "Ineligible",
              "label": "Ineligible"
            }
          },
          "type_name": "Traffic Offense",
          "expungement_rules": "A conviction for a State or municipal traffic offense is not eligible for expungement. Common convictions under this category include Driving While Suspended/Revoked, Possession of a Stolen Vehicle, Driving Under the Influence of Intoxicants, and Failure to Perform Duties of a Driver."
        },
        {
          "id": "X0001-2-0",
          "name": "Violation Driving While Suspended or Revoked",
          "statute": "811175",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Dismissed",
            "status": "Dismissed",
            "amended": false
          },
          "ambiguous_charge_id": "X0001-2",
          "case_number": "X0001",
          "expungement_result": {
            "type_eligibility": {
              "status": "Eligible",
              "reason": "Dismissals are generally eligible under 137.225(1)(b)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Ten years from most recent conviction (137.225(7)(b))",
              "date_will_be_eligible": "Jun 12, 2027"
            },
            "charge_eligibility": {
              "status": "Will be eligible",
              "label": "Eligible Jun 12, 2027"
            }
          },
          "type_name": "Dismissed Criminal Charge",
          "expungement_rules": "All non-duii criminal charges that are dismissed fall under this charge type."
        },
        {
          "id": "X0001-3-0",
          "name": "Failure to Obey Traffic Control Device",
          "statute": "811265",
          "level": "Class B Felony",
          "date": "Mar 12, 2017",
          "disposition": {
            "date": "Jun 12, 2017",
            "ruling": "Acquitted",
            "status": "Dismissed",
            "amended": false
          },
          "ambiguous_charge_id": "X0001-3",
          "case_number": "X0001",
          "expungement_result": {
            "type_eligibility": {
              "status": "Eligible",
              "reason": "Dismissals are generally eligible under 137.225(1)(b)"
            },
            "time_eligibility": {
              "status": "Ineligible",
              "reason": "Ten years from most recent conviction (137.225(7)(b))",
              "date_will_be_eligible": "Jun 12, 2027"
            },
            "charge_eligibility": {
              "status": "Will be eligible",
              "label": "Eligible Jun 12, 2027"
            }
          },
          "type_name": "Dismissed Criminal Charge",
          "expungement_rules": "All non-duii criminal charges that are dismissed fall under this charge type."
        }
      ]
    }
  ],
  "errors": []
}"""
    assert json.loads(json.dumps(record_with_various_categories, cls=ExpungeModelEncoder)) == json.loads(record_dump)
