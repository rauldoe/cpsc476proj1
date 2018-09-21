from flask import jsonify

from objectBase import objectBase

class forum(objectBase):

    def __init__(self, id, name, creator):
        super().__init__(id)

        self.name = name
        self.creator = creator

    nameTag = "name"
    @property
    def name(self):
        return self.objectLookup[self.nameTag]

    @name.setter
    def name(self, value):
        self.objectLookup[self.nameTag] = value
    
    creatorTag = "creator"
    @property
    def creator(self):
        return self.objectLookup[self.creatorTag]

    @creator.setter
    def creator(self, value):
        self.objectLookup[self.creatorTag] = value

    @staticmethod
    def deserialize(jsonObj):
        return forum(0, jsonObj["name"], "")

