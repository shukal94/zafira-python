class BaseType:
    """
    Base type state, stores an id
    """
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id
