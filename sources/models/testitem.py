from sources.lib.dto import DTO


class Test:

    def __init__(self, id, name, test_run_id, test_case_id):
        self.__id = id
        self.__name = name
        self.__test_run_id = test_run_id
        self.__test_case_id = test_case_id

        self.__dto = DTO(id=self.__id,
                         name=self.__name,
                         testRunId=self.__test_run_id,
                         test_case_id=self.__test_case_id)

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
