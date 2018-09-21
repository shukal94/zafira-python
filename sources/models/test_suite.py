from .base_type import BaseType


class TestSuite(BaseType):
    """
    Stores info about a state of test suite
    """
    def __init__(self, id, name, filename, description, user_id):
        BaseType.__init__(self, id)
        self.__name = name
        self.__filename = filename
        self.__description = description
        self.__user_id = user_id

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
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

