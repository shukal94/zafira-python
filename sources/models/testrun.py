from sources.models.base_type import BaseType
from sources.models.enums import Initiator, DriverMode

class TestRun(BaseType):

    def __init__(self, id, ciRunId, testSuiteId, status, scmURL, scmBranch, scmCommit, configXML, jobId, upstreamJobId,
                 upstreamJobBuildNumber, buildNumber, startedBy, userId, workItem, project, knownIssue, blocker,
                 driverMode, reviewed):
        BaseType.__init__(id)
        self.ciRunId = ciRunId
        self.testSuiteId = testSuiteId
        self.status = status
        self.scmURL = scmURL
        self.scmBranch = scmBranch
        self.scmCommit = scmCommit
        self.configXML = configXML
        self.jobId = jobId
        self.upstreamJobId = upstreamJobId
        self.upstreamJobBuildNumber = upstreamJobBuildNumber
        self.buildNumber = buildNumber
        self.startedBy = startedBy
        self.userId = userId
        self.workItem = workItem
        self.project = project
        self.knownIssue = knownIssue
        self.blocker = blocker
        self.driverMode = driverMode
        self.reviewed = reviewed

    def __init__(self, testSuiteId, jobId, buildNumber, driverMode = DriverMode.METHOD_MODE.value, startedBy=Initiator.SCHEDULER.value):
        self.testSuiteId = testSuiteId
        self.jobId = jobId
        self.buildNumber = buildNumber
        self.startedBy = startedBy
        self.driverMode = driverMode
