from .base_type import BaseType


class Test(BaseType):
    """
    Stores info about a state of test
    """
    def __init__(self, id, name, status, test_args, test_run_id, test_case_id, test_group, message,
                 message_hashcode, start_time, finish_time, work_items_list, retry, config_xml, known_issue, blocker,
                 need_rerun, depends_on_methods, test_class, artifacts):
        BaseType.__init__(self, id)
        self.__name = name
        self.__status = status
        self.__test_args = test_args
        self.__test_run_id = test_run_id
        self.__test_case_id = test_case_id
        self.__test_group = test_group
        self.__message = message
        self.__message_hashcode = message_hashcode
        self.__start_time = start_time
        self.__finish_time = finish_time
        self.__work_items_list = work_items_list #TODO: add to dto
        self.__retry = retry
        self.__config_xml = config_xml #TODO: add to dto
        self.__known_issue = known_issue
        self.__blocker = blocker
        self.__need_rerun = need_rerun
        self.__depends_on_methods = depends_on_methods
        self.__test_class = test_class
        self.__artifacts = artifacts #TODO: add to dto

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def test_args(self):
        return self.__test_args

    @test_args.setter
    def test_args(self, test_args):
        self.__test_args = test_args

    @property
    def test_run_id(self):
        return self.__test_run_id

    @test_run_id.setter
    def test_run_id(self, test_run_id):
        self.__test_run_id = test_run_id

    @property
    def test_case_id(self):
        return self.__test_case_id

    @test_case_id.setter
    def test_case_id(self, test_case_id):
        self.__test_case_id = test_case_id

    @property
    def test_group(self):
        return self.__test_group

    @test_group.setter
    def test_group(self, test_group):
        self.__test_group = test_group

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def message_hashcode(self):
        return self.__message_hashcode

    @message_hashcode.setter
    def message_hashcode(self, message_hashcode):
        self.__message_hashcode = message_hashcode

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def finish_time(self):
        return self.__finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        self.__finish_time = finish_time

    #TODO: add workitems, config and artifacts

    @property
    def retry(self):
        return self.__retry

    @retry.setter
    def retry(self, retry):
        self.__retry = retry

    @property
    def known_issue(self):
        return self.__known_issue

    @known_issue.setter
    def known_issue(self, known_issue):
        self.__known_issue = known_issue

    @property
    def blocker(self):
        return self.__blocker

    @blocker.setter
    def blocker(self, blocker):
        self.__blocker = blocker

    @property
    def need_rerun(self):
        return self.__need_rerun

    @need_rerun.setter
    def need_rerun(self, need_rerun):
        self.__need_rerun = need_rerun

    @property
    def depends_on_methods(self):
        return self.__depends_on_methods

    @depends_on_methods.setter
    def depends_on_methods(self, depends_on_methods):
        self.__depends_on_methods = depends_on_methods

    @property
    def test_class(self):
        return self.__test_class

    @test_class.setter
    def test_class(self, test_class):
        self.__test_class = test_class
