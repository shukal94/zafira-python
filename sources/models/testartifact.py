from sources.lib.dto import DTO


class TestArtifact:
    """
    Stores a user data
    """
    def __init__(self, id, name, link, test_id):
        self.__id = id
        self.__name = name
        self.__link = link
        self.__test_id = test_id

        self.__dto = DTO(id=self.__id,
                         name=self.__name,
                         link=self.__link,
                         testId=self.__test_id)

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