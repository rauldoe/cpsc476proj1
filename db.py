import sqlite3

from commonUtility import commonUtility

class db:

    @staticmethod
    def executeInsert(dbPath, obj):

        pLookup = obj.objectPropertyList

        columnList = ', '.join(map(lambda i: i, pLookup))
        valueList = ', '.join(map(lambda i: "'{val}'".format(val=commonUtility.getValuefromKeyValueString(pLookup, i)), pLookup))

        query = "INSERT INTO {tableName}({columnList}) VALUES({valueList});".format(tableName=obj.objectName, columnList=columnList, valueList=valueList)
        print(query)

        conn = db.initDb(dbPath)
        id = db.executeReturnId(conn, query)
        db.closeDb(conn)

        obj.id = id
    
        return obj

    #executeScriptPath("proj1.db", "init.sql")
    @staticmethod
    def executeScriptPath(dbPath, scriptPath):

        conn = db.initDb(dbPath)
        script = db.loadFile(scriptPath)
        db.executeScript(conn, script)
        db.closeDb(conn)

    #support functions
    @staticmethod
    def valueList(obj):
        pLookup = obj.objectPropertyList

        return ', '.join(map(lambda i: "'{val}'".format(val=commonUtility.getValuefromKeyValueString(pLookup, i)), pLookup))
    
    @staticmethod
    def getValue(pLookup, i):
        return commonUtility.getValuefromKeyValueString(pLookup, i)

    @staticmethod
    def initDb(dbPath):
        conn = sqlite3.connect(
                dbPath,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def closeDb(conn):
        conn.commit()
        conn.close()

    @staticmethod
    def execute(conn, query):
        cur = conn.cursor()
        cur.execute(query)

        return cur

    @staticmethod
    def executeIfExist(conn, query):
        cur = db.execute(conn, query)
        item = cur.fetchone()
        cur.close()

        if item is None:
            return False
        else:
            return True

    @staticmethod
    def executeReturnOne(conn, query):
        cur = db.execute(conn, query)
        item = cur.fetchone()
        cur.close()

        return item
    
    @staticmethod
    def executeReturnList(conn, query):
        cur = db.execute(conn, query)
        return cur.fetchall()

    @staticmethod
    def executeNonQuery(conn, query):
        cur = db.execute(conn, query)
        cur.close()

    @staticmethod
    def executeReturnId(conn, query):
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        id = cur.lastrowid
        cur.close()

        return id
    
    @staticmethod
    def executeScript(conn, queryFromScript):
        cur = conn.cursor()
        cur.executescript(queryFromScript)
        cur.close()

    @staticmethod
    def loadFile(filePath):
        data = ""

        with open(filePath, 'r') as filePtr:
            data = filePtr.read().replace('\n', '')

        return data
