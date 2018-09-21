from .base_type import BaseType


class TestArtifact(BaseType):
    """
    Stores a user data
    """
    def __init__(self, id, name, link, test_id):
        BaseType.__init__(self, id)
        self.__name = name
        self.__link = link
        self.__test_id = test_id

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
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        self.__link = link

    @property
    def test_id(self):
        return self.__test_id

    @test_id.setter
    def test_id(self, test_id):
        self.__test_id = test_id
