from flask_basicauth import BasicAuth

from db import db
from user import user
from infrastructure import infrastructure
from objectUtility import objectUtility

#app.config['BASIC_AUTH_FORCE'] = True

class cpsc476Auth(BasicAuth):

    def __init__(self, app=None):
        self.app = app
        self.username = ""
        self.dbPath = infrastructure.getDbCommon()
        super().__init__(app)

    #override parent function
    def check_credentials(self, username, password):
        obj = user()

        obj.username = username
        obj.password = password

        query = objectUtility.getExistQuery(obj, ["username", "password"])

        doesExist = db.executeIfExist(self.dbPath, query)

        if doesExist:
            self.username = obj.username
            self.app.config['BASIC_AUTH_USERNAME'] = username
            return True
        else:
            return False