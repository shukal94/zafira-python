class BaseType:
    """
    Base type state, stores an id
    """
    def __init__(self, id):
        self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id
