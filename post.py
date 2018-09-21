import datetime
from flask import jsonify
from commonUtility import commonUtility

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
        thread_id = commonUtility.dictGetSafe(jsonObj, "thread_id")
        text1 = commonUtility.dictGetSafe(jsonObj, "text1")
        poster = commonUtility.dictGetSafe(jsonObj, "poster")
        timestamp1 = commonUtility.dictGetSafe(jsonObj, "timestamp1")

        return post(0, thread_id, text1, poster, timestamp1)
