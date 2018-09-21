import requests

login_path = "/api/auth/login"
test_suites_path = "/api/tests/suites"
test_cases_path = "/api/tests/cases"
jobs_path = "/api/jobs"
test_runs_path = "/api/tests/runs"
tests_path = "/api/tests"
test_finish_path = "/api/tests/{}/finish"
test_runs_finish_path = "/api/tests/runs/{}/finish"
local_url = "http://localhost:8080/zafira-ws"



class ZafiraClient:

    def __init__(self):
        self.token = self.login().json()['accessToken']

    def login(self):
        response = requests.post(local_url + login_path, json={"password": "qpsdemo", "username": "qpsdemo"})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception()


    def create_test_suite(self):
        response = requests.post(local_url + test_suites_path, json={"description": "first suite", "fileName": "string", "id": 1, "name": "THIRD", "userId": 1 }, headers = {"Authorization": "Bearer " + self.token})

        print(response.status_code)
        print(response.json())

        if int(response.status_code) == 200:
            return response.json()
        else:
            raise Exception()

    def create_test_case(self):

        response = requests.post(local_url + test_cases_path, json={"id": 0, "info": "string", "primaryOwnerId": 1, "project": {"description": "string", "id": 0, "name": "ASAPP UI" }, "secondaryOwnerId": 1, "testClass": "string", "testMethod": "string", "testSuiteId": 3 }, headers={"Authorization": "Bearer " + self.token})

        print(response.status_code)
        print(response.json())

        if int(response.status_code) == 200:
            return response.json()


    def create_job(self):
        response = requests.post(local_url + jobs_path, json = {"id": 0, "jenkinsHost": "string", "jobURL": "string", "name": "string", "userId": 1 }, headers={"Authorization": "Bearer " + self.token})
        print(response.status_code)
        print(response.json())


        if int(response.status_code) == 200:
            return response.json()
        else:
            raise Exception()

    def create_testrun(self):
        response = requests.post(local_url + test_runs_path, json= {"blocker": "false", "buildNumber": 1, "ciRunId": "0", "configXML": "string", "driverMode": "METHOD_MODE", "id": 0, "jobId": 2, "knownIssue": "true", "project": { "description": "string", \
     "id": 0, \
     "name": "string" \
   }, \
   "reviewed": "false", \
   "scmBranch": "string", \
   "scmCommit": "string", \
   "scmURL": "string", \
   "startedBy": "SCHEDULER", \
   "status": "UNKNOWN", \
   "testSuiteId": 3, \
   "upstreamJobBuildNumber": 0, \
   "upstreamJobId": 0, \
   "userId": 1, \
   "workItem": "string" \
 }, headers={"Authorization": "Bearer " + self.token})

        print(response.status_code)
        print(response.json())


zc = ZafiraClient()
zc.create_testrun()