class DTO:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.__dict__.update((k, 'null') for k, v in self.__dict__.items() if v is None)
