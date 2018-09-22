class BaseType:
    """
    Base type state, stores an id
    """
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
