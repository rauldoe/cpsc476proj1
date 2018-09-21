
from flask import abort

from db import db

class commonUtility:

    @staticmethod
    def dictGetSafe(dict, key):
        if key in dict:
            return dict[key]
        else:
            return None

    @staticmethod
    def ifExistDoError(dbPath, query, errorStatus):
        return commonUtility.checkIfExist(dbPath, query, errorStatus, 0)

    @staticmethod
    def ifNotExistDoError(dbPath, query, errorStatus):
        return commonUtility.checkIfExist(dbPath, query, errorStatus, 1)

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
        elif statusWhenExist == 1:
            if not doesExist:
                isPassed = False
                abort(errorStatus)

        return isPassed
