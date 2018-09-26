
from flask import abort, jsonify
import json

from db import db

class helper:

    def __init__(self, objectType):
        obj = objectType()
        self.objectType = obj.objectType
        self.objectName = obj.objectName
        self.mList = []
        
    emptyFunc = lambda: True

    @staticmethod
    def getList(dbPath, objectType, whereList):

        ilist = helper(objectType)

        query = db.getSelectQuery(objectType, whereList)
        conn = db.initDb(dbPath)
        dataList = db.executeReturnList(conn, query)
        for i in dataList:
            obj = ilist.objectType()
            #ilist.processPerProperty(lambda iobj, j: iobj.setValue(j, i[j]), helper.emptyFunc, helper.emptyFunc)
            helper.processObjectProp(obj, lambda iobj, j: iobj.setValue(j, i[j]))
            ilist.append(obj)

        db.closeDb(conn)

        return ilist

    @staticmethod
    def processObjectProp(obj, func):
        pList = obj.objectPropertyListWithId
        for i in pList:
            func(obj, i)

    @staticmethod
    def ifExistDoError(dbPath, obj, propertyTag, errorStatus):
        return helper.checkIfExistObj(dbPath, obj, propertyTag, errorStatus, 0)

    @staticmethod
    def ifNotExistDoError(dbPath, obj, propertyTag, errorStatus):
        return helper.checkIfExistObj(dbPath, obj, propertyTag, errorStatus, 1)

    @staticmethod
    def checkIfExistObj(dbPath, obj, propertyTag, errorStatus, statusWhenExist):
        query = db.getExistQuery(obj, propertyTag)
        return helper.checkIfExist(dbPath, query, errorStatus, statusWhenExist)

    @staticmethod
    def checkIfExist(dbPath, query, errorStatus, statusWhenExist):

        isPassed = True

        conn = db.initDb(dbPath)
        doesExist = db.executeIfExist(conn, query)
        db.closeDb(conn)

        if statusWhenExist == 0:
            if doesExist:
                isPassed = False
                abort(errorStatus)
        else:
            if not doesExist:
                isPassed = False
                abort(errorStatus)

        return isPassed

    def append(self, item):
        self.mList.append(item)

    def serialize(self):
        return json.dumps([i.serializeItem() for i in self.mList])

    def find(self, id):
        subList = helper(self.objectType)
        for i in iter(self.mList):
            if i.id == id:
                subList.append(i)
        return subList
    
    def process(self, listFunc, preFunc, postFunc):
        preFunc()
        for i in self.mList:
            listFunc(i)
        postFunc()

    def processPerProperty(self, propFunc, preFunc, postFunc):
        listFunc = lambda i: i.process(propFunc)
        self.process(listFunc, preFunc, postFunc)
