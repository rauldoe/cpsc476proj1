from flask import jsonify

class user:
    id = 0
    username = ""
    password = ""

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #TODO: encrypt password
    def serialize(self):
        return {
            'id': self.id, 
            'username': self.username,
            'password': self.password
        }
    
    def serializeJson(self):
        return jsonify(self.serialize())

    @staticmethod
    def deserialize(jsonObj):
        return user(0, jsonObj["username"], "")

