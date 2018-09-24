from sources.dto import DTO


class TestCase:
    """
    Stores info about a state of test case
    """
    def __init__(self, id, test_class, test_method, test_suite_id, primary_owner_id):
        self.__id = id
        self.__test_class = test_class
        self.__test_method = test_method
        self.__test_suite_id = test_suite_id
        self.__primary_owner_id = primary_owner_id

        self.test_case_dto = DTO(id=self.__id,
                                 testClass=self.__test_class,
                                 testMethod=self.__test_method,
                                 testSuiteId=self.__test_suite_id,
                                 primaryOwnerId=self.__primary_owner_id)

    @property
    def dto(self):
        """
        :return: model to send representation
        """
        return self.test_case_dto

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def test_class(self):
        return self.__test_class

    @test_class.setter
    def test_class(self, test_class):
        self.__test_class = test_class

    @property
    def test_method(self):
        return self.__test_method

    @test_method.setter
    def test_method(self, test_method):
        self.__test_method = test_method

    @property
    def test_suite_id(self):
        return self.__test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        self.__test_suite_id = test_suite_id

    @property
    def primary_owner_id(self):
        return self.__primary_owner_id

    @primary_owner_id.setter
    def primary_owner_id(self, primary_owner_id):
        self.__primary_owner_id = primary_owner_id
