
from forum import forum
from flask import jsonify

class forumList:
    list = []

    def append(self, item):
        self.list.append(item)

    def appendItem(self, id, name, creator):
        self.append(forum(id, name, creator))

    def serialize(self):
        return jsonify([i.serialize() for i in self.list])

    def find(self, id):
        subList = forumList()
        [subList.append(i) for i in self.list]
        return subList