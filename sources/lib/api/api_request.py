import enum
from sources.lib.api.creds import Creds


class ApiRequest:
    """
    Provides a base functionality of requests/response with ReST API
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
        self._url = url
        self._method = method
        self._access_token = access_token
        self._creds = Creds()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        self._access_token = access_token

    @property
    def content(self):
        return 'application/json'

    @property
    def creds(self):
        return self._creds

    @creds.setter
    def creds(self, creds):
        self._creds.username = creds.username
        self._creds.password = creds.password

    class __HttpMethods(enum.Enum):
        GET = 0,
        POST = 1,
        PUT = 2,
        DELETE = 3


if __name__ == '__main__':
    reqest = ApiRequest('sdds')
    reqest.url = 'fdfddfdf'
    print(reqest.content)
    creds = Creds()
    creds.username = 'aaa'
    creds.password = 'bbb'


    reqest.creds = creds
    print(reqest.creds)





