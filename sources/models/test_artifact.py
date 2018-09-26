from .base_type import BaseType


class TestArtifact(BaseType):
    """
    Stores a user data
    """
    def __init__(self, name, link, test_id):
        self.name = name
        self.link = link
        self.test_id = test_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_link(self):
        return self.name

    def set_link(self, name):
        self.name = name

    def get_test_id(self):
        return self.test_id

    def set_test_id(self, test_id):
        self.test_id = test_id

