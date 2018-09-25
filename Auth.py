from flask_basicauth import BasicAuth

from db import db
from user import user

#app.config['BASIC_AUTH_FORCE'] = True

class Auth(BasicAuth):

    def __init__(self, app=None):
        self.app = app
        self.username = ""
        self.dbPath = "proj1.db"
        super().__init__(app)

    #override parent function
    def check_credentials(self, username, password):
        obj = user()

        obj.username = username
        obj.password = password

        query = db.getExistQuery(obj, ["username", "password"])
        conn = db.initDb(self.dbPath)
        doesExist = db.executeIfExist(conn, query)
        db.closeDb(conn)

        if doesExist:
            self.username = obj.username
            self.app.config['BASIC_AUTH_USERNAME'] = username
            return True
        else:
            return False
