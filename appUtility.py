
from flask import abort

from commonUtility import commonUtility
from db import db
from objectList import objectList
from objectUtility import objectUtility

class appUtility:

    emptyFunc = lambda: True

    @staticmethod    
    def loadList(dbPath, objectType, whereList):

        ilist = objectList(objectType)

        query = objectUtility.getSelectQuery(objectType, whereList)

        dataList = db.executeReturnList(dbPath, query)
        for i in dataList:
            obj = ilist.objectType()
            #ilist.processPerProperty(lambda iobj, j: iobj.setValue(j, i[j]), appUtility.emptyFunc, appUtility.emptyFunc)
            appUtility.processObjectProp(obj, lambda iobj, j: iobj.setValue(j, i[j]))
            ilist.append(obj)

        return ilist

    @staticmethod
    def processObjectProp(obj, func):
        pList = obj.objectPropertyListWithId
        for i in pList:
            func(obj, i)

    @staticmethod
    def ifExistDoError(dbPath, obj, propertyTag, errorStatus):
        return appUtility.checkIfExistObj(dbPath, obj, propertyTag, errorStatus, 0)

    @staticmethod
    def ifNotExistDoError(dbPath, obj, propertyTag, errorStatus):
        return appUtility.checkIfExistObj(dbPath, obj, propertyTag, errorStatus, 1)

    @staticmethod
    def checkIfExistObj(dbPath, obj, propertyTag, errorStatus, statusWhenExist):
        query = objectUtility.getExistQuery(obj, propertyTag)
        return appUtility.checkIfExist(dbPath, query, errorStatus, statusWhenExist)

    @staticmethod
    def checkIfExist(dbPath, query, errorStatus, statusWhenExist):

        isPassed = True

        doesExist = db.executeIfExist(dbPath, query)

        if statusWhenExist == 0:
            if doesExist:
                isPassed = False
                abort(errorStatus)
        else:
            if not doesExist:
                isPassed = False
                abort(errorStatus)
        
        return isPassed
