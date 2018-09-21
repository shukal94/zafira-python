from .base_type import BaseType


class Job(BaseType):
    """
    Stores a job data
    """
    def __init__(self, id, name, job_url, jenkins_host, user_id):
        BaseType.__init__(self, id)
        self.__name = name
        self.__job_url = job_url
        self.__link = jenkins_host
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def job_url(self):
        return self.__job_url

    @job_url.setter
    def job_url(self, job_url):
        self.__job_url = job_url

    @property
    def jenkins_host(self):
        return self.__link

    @jenkins_host.setter
    def jenkins_host(self, jenkins_host):
        self.__link = jenkins_host

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id