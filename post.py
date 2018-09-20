import datetime
from flask import jsonify

class post:
    id = 0
    thread_id = 0
    title = ""
    text1 = ""
    author = ""
    timestamp1 = datetime.datetime.now()

    def __init__(self, id, thread_id, text1, poster, timestamp1):
        self.id = id
        self.thread_id = thread_id
        self.text1 = text1
        self.poster = poster
        self.timestamp1 = timestamp1

    def serialize(self):
        return {
            'id': self.id, 
            'thread_id': self.thread_id,
            'text1': self.text1,
            'poster': self.poster,
            'timestamp1': self.timestamp1
        }
    
    def serializeJson(self):
        return jsonify(self.serialize())

    @staticmethod
    def deserialize(jsonObj):
        return post(0, jsonObj["thread_id"],jsonObj["text1"],jsonObj["poster"],jsonObj["timestamp1"])

