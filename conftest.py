import time
import pytest

from random import randint

from sources.client.zafira_client import ZafiraClient
from sources.models.enums import TestStatus
from sources.models.job import Job
from sources.models.test import Test
from sources.models.test_artifact import TestArtifact
from sources.models.test_case import TestCase
from sources.models.test_suite import TestSuite
from sources.models.testrun import TestRun
from sources.models.user import User

zc = ZafiraClient("http://demo.qaprosoft.com/zafira-ws")
test_suite_id = None
test_case_id = None
job_id = None
test_run_id = None
test_id = None
test = None
full_path_to_artifact = '/Users/kbugrim/Documents/projects/asap/asapp-qa/logs/'


@pytest.hookimpl
def pytest_sessionstart(session):
    user = User('admin', 'changeit')
    test_suite = TestSuite("hssff1z", "ASAP - tests", "1")
    zc.token = zc.login(user).json()['accessToken']
    response_test_suite = zc.create_test_suite(test_suite)
    test_suite_id = response_test_suite.json()['id']
    test_case = TestCase("tessfsfgtClass2", "methfsgssgodName", test_suite_id, "1")
    response_test_case = zc.create_test_case(test_case)
    global test_case_id
    test_case_id = response_test_case.json()['id']
    job = Job(session.name, 'jobsgUrsfl', 'jenkisgns1Ho1eqst', '1')
    response_job = zc.create_job(job)
    global job_id
    job_id = response_job.json()['id']
    test_run = TestRun(test_suite_id, job_id, 1)
    response_test_run = zc.create_testrun(test_run)
    global test_run_id
    test_run_id = response_test_run.json()['id']

@pytest.hookimpl
def pytest_runtest_call(item):
    global test
    test = Test("For finish new1", str(test_run_id), str(1))
    test.set_startTime(round(time.time() * 1000))
    test.set_name(item.name)
    response_test = zc.start_test(test)
    global test_id
    test_id = response_test.json()['id']
    test.set_id(test_id)

@pytest.hookimpl
def pytest_runtest_teardown(item):
    zc.finish_test(test)

@pytest.hookimpl
def pytest_runtest_logreport(report):
    global test
    if report.when == 'call':
        test.set_finishTime(round(time.time() * 1000))
        if report.outcome == 'passed':
            test.set_status(TestStatus.PASSED.value)
        elif report.outcome == 'failed':
            test.set_status(TestStatus.FAILED.value)
            test.set_message(report.longreprtext)

        name = str(randint(10000, 100000))
        link = full_path_to_artifact + name

        with open(link, 'w') as outfile:
            outfile.write(report.capstdout)
        test_artifact = TestArtifact('logs', 'file://' + link, str(test_id))
        zc.add_test_artifact_to_test(test_id, test_artifact)


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    zc.finish_testrun(test_run_id)
