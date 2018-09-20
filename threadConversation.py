import datetime
from flask import jsonify

class threadConversation:
    id = 0
    forum_id = 0
    title = ""
    text1 = ""
    author = ""
    timestamp1 = datetime.datetime.now()

    def __init__(self, id, forum_id, title, text1, author, timestamp1):
        self.id = id
        self.forum_id = forum_id
        self.title = title
        self.text1 = text1
        self.author = author
        self.timestamp1 = timestamp1

    def serialize(self):
        return {
            'id': self.id, 
            'forum_id': self.forum_id,
            'title': self.title,
            'text1': self.text1,
            'author': self.author,
            'timestamp1': self.timestamp1
        }
    
    def serializeJson(self):
        return jsonify(self.serialize())

    @staticmethod
    def deserialize(jsonObj):
        return threadConversation(0, jsonObj["forum_id"], jsonObj["title"], jsonObj["text"],jsonObj["author"], jsonObj["timestamp1"])

