from sources.models.base_type import BaseType


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
        # self.status = TestStatus.IN_PROGRESS.value

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
