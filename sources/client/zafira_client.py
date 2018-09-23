import requests
from sources.models.user import User
from sources.models.enums import TestStatus
from sources.models.job import Job
from sources.models.test import Test
from sources.models.test_case import TestCase
from sources.models.test_suite import TestSuite
from sources.models.testrun import TestRun
import time


login_path = "/api/auth/login"
test_suites_path = "/api/tests/suites"
test_cases_path = "/api/tests/cases"
jobs_path = "/api/jobs"
test_runs_path = "/api/tests/runs"
tests_path = "/api/tests"
test_finish_path = "/api/tests/{}/finish"
test_runs_finish_path = "/api/tests/runs/{}/finish"
test_runs_abort_path = "/api/tests/runs/abort?id={}"
test_by_id_path = "/api/tests/{}"
local_url = "http://localhost:8080/zafira-ws"
bearer_authorization = "Bearer "


class ZafiraClient:
    token = ''

    def __init__(self):
        pass

    def login(self, user):
        response = requests.post(local_url + login_path, json=user.__dict__)
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def create_test_suite(self, test_suite):
        response = requests.post(local_url + test_suites_path, json=test_suite.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def create_test_case(self, test_case):
        response = requests.post(local_url + test_cases_path, json=test_case.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response

    def create_job(self, job):
        response = requests.post(local_url + jobs_path, json=job.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def create_testrun(self, test_run):
        response = requests.post(local_url + test_runs_path, json=test_run.__dict__,
                                 headers={"Authorization": "Bearer " + self.token})
        return response

    def finish_testrun(self, id):
        response = requests.post(local_url + test_runs_finish_path.format(str(id)),
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def abort_testrun(self, id):
        response = requests.post(local_url + test_runs_abort_path.format(str(id)),
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def start_test(self, test):
        response = requests.post((local_url + tests_path), json=test.__dict__,
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()



    def finish_test(self, test):
        response = requests.post((local_url + test_finish_path.format(test.get_id())), json=test.__dict__,
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()


    def finish_test(self, test):
        response = requests.post((local_url + test_finish_path.format(test.get_id())), json=test.__dict__,
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()


    def delete_test_by_id(self, id):
        response = requests.delete((local_url + test_by_id_path.format(str(id))),
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()


    def update_test(self, test):
        response = requests.put((local_url + tests_path), json=test.__dict__,
                                 headers={"Authorization": "Bearer " + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()







user = User('qpsdemo', 'qpsdemo')
test_suite = TestSuite("h1z", "ASAP - smoke Tests", "1")

zc = ZafiraClient()
zc.token = zc.login(user).json()['accessToken']
response_test_suite = zc.create_test_suite(test_suite)
test_suite_id = response_test_suite.json()['id']

test_case = TestCase("testClass2", "methodName", test_suite_id, "1")

response_test_case = zc.create_test_case(test_case)
test_case_id = response_test_case.json()['id']

job = Job('jobName2', 'jobUrl3', 'jenkinsHo1st', '1')
response_job = zc.create_job(job)
job_id = response_job.json()['id']

test_run = TestRun(test_suite_id, job_id, 1)
response_test_run = zc.create_testrun(test_run)

test_run_id = response_test_run.json()['id']

test = Test("For finish new1", str(test_run_id), str(1))

response_test = zc.start_test(test)
test_id = response_test.json()['id']
time.sleep(5)


test.set_id(test_id)
test.set_status(TestStatus.PASSED.value)
test.set_finishTime(round(time.time() * 1000))
zc.finish_test(test)
# test.set_status(TestStatus.SKIPPED.value)
# zc.update_test(test)
#
# zc.finish_testrun(test_run_id)


test.set_id()

