
from objectBase import objectBase

class user(objectBase):


    def __init__(self):
        super().__init__()

        self.objectLookup[self.username_tag] = None
        self.objectLookup[self.password_tag] = None
    
    username_tag = "username"
    @property
    def username(self):
        return self.objectLookup[self.username_tag]

    @username.setter
    def username(self, value):
        self.objectLookup[self.username_tag] = value

    password_tag = "password"
    @property
    def password(self):
        return self.objectLookup[self.password_tag]

    @password.setter
    def password(self, value):
        self.objectLookup[self.password_tag] = value