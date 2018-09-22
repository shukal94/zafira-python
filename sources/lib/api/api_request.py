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

    def execute(self, json=None, cookies=None):
        """
        Basic executor for http request to target url
        :param cookies: authorization token by default is null (f.e. for login)
        :param json: user data
        :return: response body in json format
        """
        return requests.request(self.__method, self.__url, json=json, cookies=cookies)


if __name__ == '__main__':
    req = ApiRequest('http://demo.qaprosoft.com/zafira-ws/api/auth/login', 'POST')
    creds = Creds('admin', 'changeit')
    resp = req.execute(json=creds.__dict__)
    print(resp.json())






