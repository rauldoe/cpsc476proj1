
from forum import forum
from flask import jsonify

class forumList:
<<<<<<< HEAD
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
=======
    list = []

    def append(self, item):
        self.list.append(item)
>>>>>>> ff8cd2ac16674d6b2abb19656f5e39b069fb8d07

    def appendItem(self, id, name, creator):
        self.append(forum(id, name, creator))

    def serialize(self):
<<<<<<< HEAD
        return jsonify([i.serialize() for i in self.mList])

    def find(self, id):
        subList = forumList()
        for i in iter(self.mList):
            if i.id == id:
                subList.append(i)
        return subList
=======
        return jsonify([i.serialize() for i in self.list])

    def find(self, id):
        subList = forumList()
        [subList.append(i) for i in self.list]
        return subList
>>>>>>> ff8cd2ac16674d6b2abb19656f5e39b069fb8d07
