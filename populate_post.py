
import uuid
import datetime

from infrastructure import infrastructure
from db import db

class populate_post:

    @staticmethod
    def populate():

        insertQuery = "INSERT INTO posts(id, thread_id, text, poster, timestamp)" + " " + "VALUES (?, ?, ?, ?, ?);"

        db.configureForGUID()

        dbPath = infrastructure.getDb(1)

        data = (uuid.uuid4(), 1, 'my text1', 'poster1', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 4, 'my text2', 'poster2', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 7, 'my text3', 'poster3', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        dbPath = infrastructure.getDb(2)

        data = (uuid.uuid4(), 2, 'my text4', 'poster4', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 5, 'my text5', 'poster5', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 8, 'my text6', 'poster6', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        dbPath = infrastructure.getDb(3)

        data = (uuid.uuid4(), 3, 'my text7', 'poster7', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 6, 'my text8', 'poster8', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
        data = (uuid.uuid4(), 9, 'my text9', 'poster9', datetime.datetime.now())
        db.executeInsertWithQuery(dbPath, insertQuery, data)
        
