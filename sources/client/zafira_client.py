import requests
from sources.models.creds import Creds
from sources.models.job import Job
from sources.models.test_case import TestCase
from sources.models.test_suite import TestSuite
from sources.models.testrun import TestRun

login_path = "/api/auth/login"
test_suites_path = "/api/tests/suites"
test_cases_path = "/api/tests/cases"
jobs_path = "/api/jobs"
test_runs_path = "/api/tests/runs"
tests_path = "/api/tests"
test_finish_path = "/api/tests/{}/finish"
test_runs_finish_path = "/api/tests/runs/{}/finish"
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
        response = requests.post(local_url + test_suites_path, json=test_suite.__dict__, headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def create_test_case(self, test_case):
        response = requests.post(local_url + test_cases_path, json=test_case.__dict__, headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response


    def create_job(self, job):
        response = requests.post(local_url + jobs_path, json=job.__dict__, headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()

    def create_testrun(self, test_run):
        response = requests.post(local_url + test_runs_path, json=test_run.__dict__, headers={"Authorization": "Bearer " + self.token})
        return  response



user = Creds('qpsdemo', 'qpsdemo')
test_suite = TestSuite("h1z", "n1ext", "1")

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
print(test_run.__dict__)
response_test_run = zc.create_testrun(test_run)


print(response_test_run.status_code)




