import os
from tempfile import mkdtemp
from zipfile import ZipFile

from expungeservice.expunger import Expunger
from expungeservice.form_filling import FormFilling
from expungeservice.record_merger import RecordMerger
from expungeservice.record_summarizer import RecordSummarizer
from tests.factories.crawler_factory import CrawlerFactory
from tests.fixtures.case_details import CaseDetails
from tests.fixtures.john_doe import JohnDoe
from tests.test_crawler_expunger import record_with_mj_over_21


def test_normal_conviction_uses_multnomah_conviction_form():
    record = CrawlerFactory.create(JohnDoe.SINGLE_CASE_RECORD, {"CASEJD1": CaseDetails.CASEJD74})
    expunger_result = Expunger.run(record)
    merged_record = RecordMerger.merge([record], [expunger_result], [])
    record_summary = RecordSummarizer.summarize(merged_record, {})
    user_information = {
        "full_name": "",
        "date_of_birth": "",
        "mailing_address": "",
        "phone_number": "",
        "city": "",
        "state": "",
        "zip_code": "",
    }
    zip_path, zip_name = FormFilling.build_zip(record_summary, user_information)
    temp_dir = mkdtemp()
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)
        for _root, _dir, files in os.walk(temp_dir):
            assert len(files) == 1
            assert "multnomah_conviction" in files[0]


def test_marijuana_violation_uses_statewide_form(record_with_mj_over_21):
    expunger_result = Expunger.run(record_with_mj_over_21)
    merged_record = RecordMerger.merge([record_with_mj_over_21], [expunger_result], [])
    record_summary = RecordSummarizer.summarize(merged_record, {})
    user_information = {
        "full_name": "",
        "date_of_birth": "",
        "mailing_address": "",
        "phone_number": "",
        "city": "",
        "state": "",
        "zip_code": "",
    }
    zip_path, zip_name = FormFilling.build_zip(record_summary, user_information)
    temp_dir = mkdtemp()
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)
        for _root, _dir, files in os.walk(temp_dir):
            assert len(files) == 1
            assert "statewide_marijuana_conviction" in files[0]
