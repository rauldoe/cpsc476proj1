
from forum import forum
from flask import jsonify

class forumList:
    mList = []

    def __init__(self):
        self.mList = []

    @staticmethod
    def test():
    
        ilist = forumList()
        ilist.appendItem(1, "name1", "creator1")
        ilist.appendItem(2, "name2", "creator2")
        ilist.appendItem(3, "name3", "creator3")

        return ilist

    def append(self, item):
        self.mList.append(item)

    def appendItem(self, id, name, creator):
        self.append(forum(id, name, creator))

    def serialize(self):
        return jsonify([i.serialize() for i in self.mList])

    def find(self, id):
        subList = forumList()
        for i in iter(self.mList):
            if i.id == id:
                subList.append(i)
        return subList
