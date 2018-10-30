
import sqlite3
import uuid

from commonUtility import commonUtility

class db:

    #PUBLIC METHODS FOR OBJECTS BEGIN
    @staticmethod
    def executeInsert(dbPath, obj):

        pLookup = obj.objectPropertyList

        columnList = ', '.join(map(lambda i: i, pLookup))
        valueList = ', '.join(map(lambda i: "'{val}'".format(val=commonUtility.getValuefromKeyValueString(pLookup, i)), pLookup))

        query = "INSERT INTO {tableName}({columnList}) VALUES({valueList});".format(tableName=obj.objectEntity, columnList=columnList, valueList=valueList)
        #print(query)

        conn = db.__initDb(dbPath)
        id = db.__executeReturnId(conn, query)
        db.__closeDb(conn)

        obj.id = id
    
        return obj

    @staticmethod
    def executeInsertWithId(dbPath, obj):

        pLookup = obj.objectPropertyListWithId
        data = obj.objectValueArrayWithId

        columnList = ', '.join(map(lambda i: i, pLookup))
        valueList = ', '.join(map(lambda i: "?", pLookup))

        #data = (uuid.uuid4(), 4, 'my text2', 'poster2', datetime.datetime.now())
        #db.executeInsertWithQuery(dbPath, insertQuery, data)

        query = "INSERT INTO {tableName}({columnList}) VALUES({valueList});".format(tableName=obj.objectEntity, columnList=columnList, valueList=valueList)
        #print(query)

        db.executeInsertWithQuery(dbPath, query, data)

        #obj.id = id
    
        return obj

    #UPDATE table_name
    #SET column1 = value1, column2 = value2, ...
    #WHERE condition;
    @staticmethod
    def executeUpdate(dbPath, obj, whereList):

        pLookup = obj.objectPropertyList
        if len(whereList) > 0:
            whereClause = " WHERE {listString}".format(listString=' AND '.join(map(lambda i: "{col} = '{val}'".format(col=i, val=obj.getValue(i)), whereList)))
        else:
            whereClause = ""

        valueSetList = ', '.join(map(lambda i: "{col} = '{val}'".format(col=i, val=commonUtility.getValuefromKeyValueString(pLookup, i)), pLookup))

        query = "UPDATE {tableName} SET {valueSetList}{whereClause};".format(tableName=obj.objectEntity, valueSetList=valueSetList, whereClause=whereClause)
        print(query)

        conn = db.__initDb(dbPath)
        db.__executeNonQuery(conn, query)
        db.__closeDb(conn)
    
        return obj
    #PUBLIC METHODS FOR OBJECTS END

    #PUBLIC METHODS START
    @staticmethod
    def configureForGUID():
        sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
        sqlite3.register_adapter(uuid.UUID, lambda u: u.bytes_le)

    #executeScriptPath("proj1.db", "init.sql")
    @staticmethod
    def executeScriptPath(dbPath, scriptPath):

        conn = db.__initDb(dbPath)
        script = commonUtility.loadFile(scriptPath)
        cursor = conn.cursor()
        cursor.executescript(script)
        cursor.close()
        db.__closeDb(conn)

    @staticmethod
    def executeInsertWithQuery(dbPath, insertQuery, data):
        conn = db.__initDb(dbPath)
        db.__executeInsertWithQuery(conn, insertQuery, data)
        db.__closeDb(conn)

    @staticmethod
    def executeIfExist(dbPath, query):
        conn = db.__initDb(dbPath)
        cursor = db.__execute(conn, query)
        item = cursor.fetchone()
        cursor.close()
        db.__closeDb(conn)

        if item is None:
            return False
        else:
            return True
    
    @staticmethod
    def executeReturnList(dbPath, query):
        conn = db.__initDb(dbPath)
        list = db.__executeReturnList(conn, query)
        db.__closeDb(conn)
        return list
    #PUBLIC METHODS END

    #PRIVATE METHODS BEGIN
    @staticmethod
    def __initDb(dbPath):
        conn = sqlite3.connect(
                dbPath,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def __execute(conn, query):
        cursor = conn.cursor()
        cursor.execute(query)

        return cursor
   
    @staticmethod
    def __executeNonQuery(conn, query):
        cursor = db.__execute(conn, query)
        cursor.close()

    @staticmethod
    def __executeReturnId(conn, query):
        cursor = db.__execute(conn, query)
        conn.commit()
        id = cursor.lastrowid
        cursor.close()

        return id

    @staticmethod
    def __executeReturnList(conn, query):
        cursor = db.__execute(conn, query)
        list = cursor.fetchall()
        cursor.close()

        return list

    @staticmethod
    def __executeInsertWithQuery(conn, insertQuery, data):

        #data = (uuid.uuid4(), 'foo')
        #conn.execute('INSERT INTO test VALUES (?,?)', data)
        print(insertQuery)
        print(data)
        cursor = conn.cursor()
        cursor.execute(insertQuery, data)
        cursor.close()

    @staticmethod
    def __closeDb(conn):
        conn.commit()
        conn.close()
    #PRIVATE METHODS END

