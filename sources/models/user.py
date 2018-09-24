class User:
    """
    Stores a user credentials
    """

    def __init__(self):
        """
        Default constructor for an empty state of creds
        """
        self.username
        self.password
        self.email
        self.firstName
        self.lastName
        self.photoURL
        self.groups
        self.preferences
        self.lastLogin
        self.tenant
        self.source
        self.status

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username


    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password


    def set_password(self, password):
        self.password = password

    def __repr__(self):
        return 'User: ' + self.username + ',\nPassword: ' + self.password
