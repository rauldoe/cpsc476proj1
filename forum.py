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

    @staticmethod
    def deserialize(json):
        return forum(0, json["name"], "")
