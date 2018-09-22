from .base_type import BaseType


class User(BaseType):
    """
    Stores a user data
    """
    def __init__(self, id, username, firstname, lastname, email, password):
        BaseType.__init__(self, id)
        self.__username = username
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email

    @property
    def id(self):
        return self.__id

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

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
