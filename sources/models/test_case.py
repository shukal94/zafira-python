from .base_type import BaseType


class TestCase(BaseType):
    """
    Stores info about a state of test case
    """
    def __init__(self, id, testClass, testMethod, info, testSuiteId, primaryOwnerId, project, secondaryOwnerId):
        BaseType.__init__(self, id)
        self.testClass = testClass
        self.testMethod = testMethod
        self.info = info
        self.testSuiteId = testSuiteId
        self.primaryOwnerId = primaryOwnerId
        self.project = project
        self.secondaryOwnerId = secondaryOwnerId

    def __init__(self, testClass, testMethod, testSuiteId, primaryOwnerId):
        self.testClass = testClass
        self.testMethod = testMethod
        self.testSuiteId = testSuiteId
        self.primaryOwnerId = primaryOwnerId


