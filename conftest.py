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

import random
from selenium import webdriver

zc = ZafiraClient("http://localhost:8080/zafira-ws")
test_suite_id = None
test_case_id = None
job_id = None
test_run_id = None
test_id = None
test = None
path_to_logs = os.getcwd() + '/reporting/logs/'
test_artifact = None



@pytest.hookimpl
def pytest_sessionstart(session):
    user = User('qpsdemo', 'qpsdemo')
    test_suite = TestSuite(0, 'h1z', session.name, '1')
    zc.token = zc.login(user).json()['accessToken']
    response_test_suite = zc.create_test_suite(test_suite)
    test_suite_id = response_test_suite.json()['id']
    test_case = TestCase(0, 'testClass2', 'methodName', test_suite_id, '1')
    response_test_case = zc.create_test_case(test_case)
    global test_case_id
    test_case_id = response_test_case.json()['id']
    job = Job(0, session.name, 'jobUrl', 'jenkinsHo1eqst', '1')
    response_job = zc.create_job(job)
    global job_id
    job_id = response_job.json()['id']
    test_run = TestRun(0, test_suite_id, job_id, 1)
    response_test_run = zc.create_testrun(test_run)
    global test_run_id
    test_run_id = response_test_run.json()['id']


@pytest.hookimpl
def pytest_runtest_call(item):
    global test
    test = Test(0, item.name, str(test_run_id), str(1), 0, 0, 'UNKNOWN')
    test.start_time = round(time.time() * 1000)
    test.name = item.name
    response_test = zc.start_test(test)
    global test_id
    test_id = response_test.json()['id']
    test.id = test_id


@pytest.hookimpl
def pytest_runtest_teardown(item):
    zc.finish_test(test)


@pytest.hookimpl
def pytest_runtest_logreport(report):
    global test
    if report.when == 'call':
        test.finish_time = round(time.time() * 1000)
        if report.outcome == 'passed':
            test.status = 'PASSED'
        elif report.outcome == 'failed':
            test.status = 'FAILED'
        # log result
        path_to_write = path_to_logs + test.name + '.log'
        with open(path_to_write, 'w') as infile:
            infile.write(report.capstdout)
            infile.write(report.capstderr)
        # add artifact
        link = 'http://locahost:8000{}'
        test_artifact = TestArtifact(0, 'logs', link.format(path_to_write), test.id)
        zc.add_test_artifact_to_test(test.id, test_artifact)


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    zc.finish_testrun(test_run_id)
