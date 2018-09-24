import time
import pytest
from sources.client.zafira_client import ZafiraClient
from sources.models.enums import TestStatus
from sources.models.job import Job
from zafira_client.models.test import Test
from zafira_client.models.test_case import TestCase
from zafira_client.models.test_suite import TestSuite
from zafira_client.models.testrun import TestRun
from zafira_client.models.user import User

zc = ZafiraClient("http://localhost:8080/zafira-ws")
test_suite_id = None
test_case_id = None
job_id = None
test_run_id = None
test_id = None
test = None


@pytest.hookimpl
def pytest_sessionstart(session):
    user = User('qpsdemo', 'qpsdemo')
    test_suite = TestSuite("h1z", "ASAP - smoke Tests", "1")
    zc.token = zc.login(user).json()['accessToken']
    response_test_suite = zc.create_test_suite(test_suite)
    test_suite_id = response_test_suite.json()['id']
    test_case = TestCase("testClass2", "methodName", test_suite_id, "1")
    response_test_case = zc.create_test_case(test_case)
    global test_case_id
    test_case_id = response_test_case.json()['id']
    job = Job(session.name, 'jobUrl', 'jenkinsHo1eqst', '1')
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


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    zc.finish_testrun(test_run_id)