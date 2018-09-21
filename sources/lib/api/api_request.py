import requests
from sources.models.creds import Creds


class ApiRequest:
    """
    Provides a base functionality of requests/response with Zafira Public API
    :author sshukalovich@qaprosoft.com:
    :date 09/19/2018:
    """
    def __init__(self, url, method='GET', access_token=''):
        """
        Constructs an instance of request
        :param url: target url-address
        :param method: GET, POST, PUT or DELETE verb - http methods
        :param access_token: uses for authenticated users
        """
        self.__url = url
        self.__method = method
        self.__access_token = access_token
        self.__creds = Creds()
        self.__project = ''
        self.__http_request = None
        self.__http_response = None
        self.__data = {}
        self.__cookie = {}

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method):
        self.__method = method

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token

    @property
    def content(self):
        return 'application/json'

    @property
    def creds(self):
        return self.__creds

    @creds.setter
    def creds(self, creds):
        self.__creds.username = creds.username
        self.__creds.password = creds.password

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, project):
        self.__project = project

    def execute(self, method, url, data=None, cookie=None):
        """
        Basic executor for http request to target url
        :param method: GET, POST, PUT or DELETE
        :param url: target url, base + endpoint
        :param cookie: authorization token by default is null (f.e. for login)
        :param data: user data
        :return: response body in json format
        """
        pass


if __name__ == '__main__':
    reqest = ApiRequest('sdds')
    reqest.url = 'fdfddfdf'
    print(reqest.content)
    creds = Creds()
    creds.username = 'aaa'
    creds.password = 'bbb'


    reqest.creds = creds
    print(reqest.creds)





