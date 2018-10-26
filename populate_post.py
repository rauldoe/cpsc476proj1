import sqlite3
import uuid
import time
import datetime

class populate_post:
    @staticmethod
    def init():
        sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
        sqlite3.register_adapter(uuid.UUID, lambda u: buffer(u.bytes_le))

    @staticmethod
    def getConnection(dbPath):
        conn = sqlite3.connect(dbPath, detect_types=sqlite3.PARSE_DECLTYPES)

        return conn.cursor()

    @staticmethod
    def runInsert(dbPath, threadId, text, poster):
        conn = populate_post.getConnection(dbPath)
        timestamp = datetime.datetime.now()
        data = (uuid.uuid4(), threadId, text, poster, timestamp)
        conn.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?)', data)

    @staticmethod
    def process():
        populate_post.init()

        dbPath = "post0.db"
        populate_post.runInsert(dbPath, 3, "mytext", "poster0")
        populate_post.runInsert(dbPath, 6, "mytext", "poster1")
        populate_post.runInsert(dbPath, 9, "mytext", "poster2")

        dbPath = "post1.db"
        populate_post.runInsert(dbPath, 1, "mytext", "poster0")
        populate_post.runInsert(dbPath, 4, "mytext", "poster1")
        populate_post.runInsert(dbPath, 7, "mytext", "poster2")


        dbPath = "post2.db"
        populate_post.runInsert(dbPath, 2, "mytext", "poster0")
        populate_post.runInsert(dbPath, 5, "mytext", "poster1")
        populate_post.runInsert(dbPath, 8, "mytext", "poster2")
