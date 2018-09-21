class Creds:
    """
    Stores a user credentials
    """

    def __init__(self):
        """
        Default constructor for an empty state of creds
        """
        self._username = ''
        self._password = ''

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __repr__(self):
        return 'User: ' + self._username + ',\nPassword: ' + self._password
