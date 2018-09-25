from reporting.sources.dto import DTO


class User:
    """
    Stores a user credentials
    """
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

        self.__dto = DTO(username=self.__username,
                         password=self.__password)

    @property
    def dto(self):
        return self.__dto

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

