import time
import pytest
import os
from reporting.sources.zafira_client import ZafiraClient
from reporting.sources.models.enums import TestStatus
from reporting.sources.models.job import Job
from reporting.sources.models.testitem import Test
from reporting.sources.models.testcase import TestCase
from reporting.sources.models.testsuite import TestSuite
from reporting.sources.models.testrun import TestRun
from reporting.sources.models.user import User
from reporting.sources.models.testartifact import TestArtifact

zc = ZafiraClient("http://localhost:8080/zafira-ws")
user = User('qpsdemo', 'qpsdemo')

test_suite_id = 0
test_case_id = 0
job_id = 0
test_run_id = ''
test_id = 0
path_to_logs = os.getcwd() + '/reporting/logs/'


@pytest.hookimpl
def pytest_sessionstart(session):
    test_suite = TestSuite(0, session.name, session.name, '1')
    zc.token = zc.login(user).json()['accessToken']
    global test_suite_id
    test_suite_id = zc.create_test_suite(test_suite).json()['id']
    test_case = TestCase(0, 'testClass2', 'methodName', test_suite_id, '1')
    global test_case_id
    test_case_id = zc.create_test_case(test_case).json()['id']
    job = Job(0, session.name, 'jobUrl', 'jenkinsHo1eqst', '1')
    global job_id
    job_id = zc.create_job(job).json()['id']
    test_run = TestRun(0, test_suite_id, job_id, 1)
    test_run.test_suite_id, test_run.job_id = str(test_suite_id), job_id
    global test_run_id
    test_run_id = zc.create_testrun(test_run).json()['id']


@pytest.hookimpl
def pytest_runtest_call(item):
    global test
    test = Test(0, '', '', 1, 0, 0, 'UNKNOWN')
    global test_run_id
    test.dto.__dict__['name'], test.dto.__dict__['startTime'], \
    test.dto.__dict__['testRunId'] = item.name, round(time.time() * 1000), test_run_id
    global test_id
    test_id = zc.start_test(test).json()['id']
    test.id = test_id


@pytest.hookimpl
def pytest_runtest_teardown(item):
    zc.finish_test(test)


@pytest.hookimpl
def pytest_runtest_logreport(report):
    if report.when == 'call':
        test.dto.__dict__['finishTime'] = round(time.time() * 1000)
        if report.outcome == 'passed':
            test.dto.__dict__['status'] = TestStatus.PASSED.value
        elif report.outcome == 'failed':
            test.dto.__dict__['status'] = TestStatus.FAILED.value
            test.dto.__dict__['message'] = report.longreprtext
        # log result
        path_to_write = path_to_logs + test.dto.__dict__['name'] + '.log'
        with open(path_to_write, 'w') as infile:
            infile.write(report.capstdout)
            infile.write(report.capstderr)
        # add artifact
        link = 'file:///{}'
        test_artifact = TestArtifact(0, 'logs', link.format(path_to_write), test.id)
        zc.add_test_artifact_to_test(test.id, test_artifact)


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    zc.finish_testrun(test_run_id)
