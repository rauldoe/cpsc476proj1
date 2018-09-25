
from flask import abort

from db import db
from objectList import objectList

class helper:

    emptyFunc = lambda: True

    @staticmethod
    def getList(dbPath, objectType, whereList):

        ilist = objectList(objectType)

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
