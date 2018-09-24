from .base_type import BaseType


class TestSuite(BaseType):


    def __init__(self, id, description, fileName, name, userId):
        BaseType.__init__(self, id)
        self.description = description
        self.fileName = fileName
        self.name = name
        self.userId = userId

    def __init__(self, description, fileName, name, userId):
        self.description = description
        self.fileName = fileName
        self.name = name
        self.userId = userId

    def __init__(self, fileName, name, userId):
        self.fileName = fileName
        self.name = name
        self.userId = userId


    def get_description(self):
        return self.description

    def get_filename(self):
        return self.fileName

    def get_name(self):
        return self.name

    def get_user_id(self):
        return self.user_id

    def set_description(self, description):
        self.description = description

    def set_filename(self, fileName):
        self.fileName = fileName

    def set_name(self, name):
        self.name = name

    def set_userId(self, userId):
        self.userId = userId
