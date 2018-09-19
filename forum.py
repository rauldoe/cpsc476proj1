from flask import jsonify

class forum:
    id = 0
    name = ""
    creator = ""

    def __init__(self, id, name, creator):
        self.id = id
        self.name = name
        self.creator = creator

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'creator': self.creator
        }
    
    def serializeJson(self):
        return jsonify(self.serialize())

    @staticmethod
    def deserialize(jsonObj):
        return forum(0, jsonObj["name"], "")

