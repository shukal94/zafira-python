from .base_type import BaseType


class TestCase(BaseType):
    """
    Stores info about a state of test case
    """
    def __init__(self, testClass, testMethod, testSuiteId, primaryOwnerId):
        self.testClass = testClass
        self.testMethod = testMethod
        self.testSuiteId = testSuiteId
        self.primaryOwnerId = primaryOwnerId


