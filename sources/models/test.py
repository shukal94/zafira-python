from zafira_client.models.base_type import BaseType


class Test(BaseType):

    def __init__(self, id, name, status, testArgs, testRunId, testCaseId, testGroup, message, messageHashCode,
                 startTime, finishTime, workItems, retry, configXML, testMetric,
                 dependsOnMethods, testClass, artifacts, needRerun=False, blocker=False, knownIssue=False):
        BaseType.__init__(self, id)
        self.name = name
        self.status = status
        self.testArgs = testArgs
        self.testRunId = testRunId
        self.testCaseId = testCaseId
        self.testGroup = testGroup
        self.message = message
        self.messageHashCode = messageHashCode
        self.startTime = startTime
        self.finishTime = finishTime
        self.workItems = workItems
        self.retry = retry
        self.configXML = configXML
        self.testMetrics = testMetric
        self.knownIssue = knownIssue
        self.blocker = blocker
        self.needRerun = needRerun
        self.dependsOnMethods = dependsOnMethods
        self.testClass = testClass
        self.artifacts = artifacts

    def __init__(self, name, testRunId, testCaseId):
        self.name = name
        self.testRunId = testRunId
        self.testCaseId = testCaseId

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_startTime(self, start_time):
        self.startTime = start_time

    def get_startTime(self):
        return self.startTime

    def set_finishTime(self, finish_time):
        self.finishTime = finish_time

    def get_finishTime(self):
        return self.finishTime

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_test_class(self, test_class):
        self.testClass = test_class

    def get_test_class(self):
        return self.testClass

    def set_artifacts(self, artifacts):
        self.artifacts = artifacts

