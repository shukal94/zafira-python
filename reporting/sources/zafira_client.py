import requests

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
test_artifact_path = "/api/tests/{}/artifacts"

bearer_authorization = "Bearer "


class ZafiraClient:

    def __init__(self, local_url):
        self.local_url = local_url
        self.token = ''

    def login(self, user):
        response = requests.post(self.local_url + login_path, json=user.dto.__dict__)
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def create_test_suite(self, test_suite):
        response = requests.post(self.local_url + test_suites_path, json=test_suite.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def create_test_case(self, test_case):
        response = requests.post(self.local_url + test_cases_path, json=test_case.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response

    def create_job(self, job):
        response = requests.post(self.local_url + jobs_path, json=job.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})

        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def create_testrun(self, test_run):
        response = requests.post(self.local_url + test_runs_path, json=test_run.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})
        return response

    def finish_testrun(self, id):
        response = requests.post(self.local_url + test_runs_finish_path.format(str(id)),
                                 headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def abort_testrun(self, id):
        response = requests.post(self.local_url + test_runs_abort_path.format(str(id)),
                                 headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def start_test(self, test):
        response = requests.post((self.local_url + tests_path), json=test.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def finish_test(self, test):
        response = requests.post(self.local_url + test_finish_path.format(test.id), json=test.dto.__dict__,
                                 headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def delete_test_by_id(self, id):
        response = requests.delete((self.local_url + test_by_id_path.format(str(id))),
                                   headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def update_test(self, test):
        response = requests.put((self.local_url + tests_path), json=test.dto.__dict__,
                                headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception

    def add_test_artifact_to_test(self, test_id, test_artifact):
        response = requests.post(self.local_url + test_artifact_path.format(str(test_id)),
                        json=test_artifact.dto.__dict__, headers={"Authorization": bearer_authorization + self.token})
        if int(response.status_code) == 200:
            return response
        else:
            raise Exception



