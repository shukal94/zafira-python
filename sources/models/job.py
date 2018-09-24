from sources.models.base_type import BaseType


class Job(BaseType):

    def __init__(self, id, name, jobURL, jenkinsHost, userId):
        BaseType.__init__(self, id)
        self.name = name
        self.jobURL = jobURL
        self.jenkinsHost = jenkinsHost
        self.userId = userId
