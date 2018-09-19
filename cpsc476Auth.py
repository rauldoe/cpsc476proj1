from flask_basicauth import BasicAuth

#app.config['BASIC_AUTH_USERNAME'] = 'john'
#app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
#app.config['BASIC_AUTH_FORCE'] = True

class cpsc476Auth(BasicAuth):
    app = None
    username = ""

    def __init__(self, app=None):
        self.app = app
        super().__init__(app)

    #override parent function
    def check_credentials(self, username, password):
        self.username = username
        self.app.config['BASIC_AUTH_USERNAME'] = username
        return True
