from sources.dto import DTO


class TestSuite:

    def __init__(self, id, file_name, name, user_id):
        self.__id = id
        self.__file_name = file_name
        self.__name = name
        self.__user_id = user_id

        self.__dto = DTO(id=self.__id,
                         fileName=self.__file_name,
                         name=self.__name,
                         userId=self.__user_id)

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
    def filename(self):
        return self.__file_name

    @filename.setter
    def filename(self, file_name):
        self.__file_name = file_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id
