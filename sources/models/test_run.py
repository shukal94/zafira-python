from .base_type import BaseType


class TestRun(BaseType):
    """
    Stores data about test run
    """
    def __init__(self, id, cirun_id, test_suite_id, user_id, scm_url, scm_branch, scm_commit, config_xml, job_id,
                 upstream_job_id, build_number, started_by, work_item):
        BaseType.__init__(self, id)
        self.__cirun_id = cirun_id
        self.__test_suite_id = test_suite_id
        self.__user_id = user_id
        self.__scm_url = scm_url
        self.__scm_branch = scm_branch
        self.__scm_commit = scm_commit
        self.__config_xml = config_xml
        self.__job_id = job_id
        self.__upstream_job_id = upstream_job_id
        self.__build_number = build_number
        self.__started_by = started_by
        self.__work_item = work_item

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def test_suite_id(self):
        return self.__test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        self.__test_suite_id = test_suite_id

    @property
    def cirun_id(self):
        return self.__cirun_id

    @cirun_id.setter
    def cirun_id(self, cirun_id):
        self.__cirun_id = cirun_id

    @property
    def scm_url(self):
        return self.__scm_url

    @scm_url.setter
    def scm_url(self, scm_url):
        self.__scm_url = scm_url

    @property
    def scm_commit(self):
        return self.__scm_commit

    @scm_commit.setter
    def scm_commit(self, scm_commit):
        self.__scm_commit = scm_commit

    @property
    def scm_branch(self):
        return self.__scm_branch

    @scm_branch.setter
    def scm_branch(self, scm_branch):
        self.__scm_branch = scm_branch

    @property
    def config_xml(self):
        return self.__config_xml

    @config_xml.setter
    def config_xml(self, config_xml):
        self.config_xml = config_xml

    @property
    def job_id(self):
        return self.__job_id

    @job_id.setter
    def job_id(self, job_id):
        self.__job_id = job_id

    @property
    def upstream_job_id(self):
        return self.__upstream_job_id

    @upstream_job_id.setter
    def upstream_job_id(self, upstream_job_id):
        self.__upstream_job_id = upstream_job_id

    @property
    def build_number(self):
        return self.__build_number

    @build_number.setter
    def build_number(self, build_number):
        self.__build_number = build_number

    @property
    def started_by(self):
        return self.__started_by

    @started_by.setter
    def started_by(self, started_by):
        self.__started_by = started_by

    @property
    def work_item(self):
        return self.__work_item

    @work_item.setter
    def work_item(self, work_item):
        self.__work_item = work_item

