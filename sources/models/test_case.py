from .base_type import BaseType


class TestCase(BaseType):
    """
    Stores info about a state of test case
    """
    def __init__(self, id, test_class, test_method, info, test_suite_id, primary_owner_id):
        BaseType.__init__(self, id)
        self.__test_class = test_class
        self.__test_method = test_method
        self.__info = info
        self.__test_suite_id = test_suite_id
        self.__primary_owner_id = primary_owner_id

    @property
    def id(self):
        return self.id

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
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info = info

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
