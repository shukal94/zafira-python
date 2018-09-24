from sources.lib.dto import DTO


class Job:

    def __init__(self, id, name, job_url, jenkins_host, user_id):
        self.__id = id
        self.__name = name
        self.__job_url = job_url
        self.__jenkins_host = jenkins_host
        self.__user_id = user_id

        self.__dto = DTO(id=self.__id,
                         name=self.__name,
                         jobURL=self.__job_url,
                         jenkinsHost=self.__jenkins_host,
                         userId=self.__user_id)

    @property
    def dto(self):
        return self.__dto

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def job_url(self):
        return self.__job_url

    @job_url.setter
    def job_url(self, job_url):
        self.__job_url = job_url

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def jenkins_host(self):
        return self.__jenkins_host

    @jenkins_host.setter
    def jenkins_host(self, jenkins_host):
        self.__jenkins_host = jenkins_host

