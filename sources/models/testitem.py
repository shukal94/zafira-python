from sources.dto import DTO


class Test:

    def __init__(self, id, name, test_run_id, test_case_id, test_artifacts=None,
                 start_time='', finish_time='', status='UNKNOWN'):
        self.__id = id
        self.__name = name
        self.__test_run_id = test_run_id
        self.__test_case_id = test_case_id
        self.__status = status
        self.__start_time = start_time
        self.__finish_time = finish_time
        self.__artifact = {artifact for artifact in test_artifacts}

        self.__dto = DTO(id=self.__id,
                         name=self.__name,
                         testRunId=self.__test_run_id,
                         test_case_id=self.__test_case_id,
                         status=self.__status,
                         startTime=self.__start_time,
                         finishTime=self.__finish_time)

    @property
    def dto(self):
        return self.__dto

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

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
