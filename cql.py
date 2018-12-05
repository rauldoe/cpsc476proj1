
from commonUtility import commonUtility
from cassandra.cluster import Cluster
from cassandra.query import dict_factory

class cql:

    @staticmethod
    def initDb(keyspace):
        cluster = Cluster()
        session = cluster.connect()

        #keyspace = "proj3"
        session.set_keyspace(keyspace)
        session.row_factory = dict_factory

        return {'cluster': cluster, 'session': session}

    @staticmethod
    def executeScriptPath(session, scriptPath):

        scriptList = commonUtility.loadFileWithDelimiter(scriptPath, ';')
        for i in scriptList:
            print(i)
            cql.execute(session, i)
        
    @staticmethod
    def execute(session, query):
        return session.execute(query)

    @staticmethod
    def executeReturnMax(session, obj):
        maxval = 0
        data = session.execute("SELECT MAX(id) AS maxval FROM {objectName};".format(objectName=obj.objectEntity))

        for i in data:
            maxval = i['maxval']
            break

        return maxval

    @staticmethod
    def executeReturnList(session, objectName):
        return session.execute("SELECT * FROM {objectName};".format(objectName=objectName))
    
    @staticmethod
    def executeReturnObjectList(session, obj):

        pLookup = obj.objectPropertyListWithId
        columnList = ', '.join(map(lambda i: i, pLookup))
        return session.execute("SELECT {columnList} FROM {objectName};".format(columnList=columnList, objectName=obj.objectEntity))

    @staticmethod
    def insertWithObjectInfo(session, objectName, parameters, parameterTagList, parameterIdList, query):

        #parameters = {}
        #parameters['id'] = id
        #parameters['thread_id'] = thread_id
        #parameters['text1'] = text1
        #parameters['poster'] = poster
        #parameters['timestamp1'] = timestamp1

        parameterTagList = "id, thread_id, text1, poster, timestamp1"
        parameterIdList = "%(id)s, %(thread_id)s, %(text1)s, %(poster)s, %(timestamp1)s"
        query = """
            INSERT INTO {objectName} ({parameterTagList})
                VALUES ({parameterIdList})
        """.format(objectName=objectName, parameterTagList=parameterTagList, parameterIdList=parameterIdList)
        
        session.execute(query, parameters)

    @staticmethod
    def insertObject(session, obj):

        pLookup = obj.objectPropertyListWithId

        parameterTagList = ', '.join(map(lambda i: i, pLookup))
        parameterIdList = ', '.join(map(lambda i: "%({j})s".format(j=i), pLookup))
        
        query = """
            INSERT INTO {objectName} ({parameterTagList})
                VALUES ({parameterIdList})
        """.format(objectName=obj.objectEntity, parameterTagList=parameterTagList, parameterIdList=parameterIdList)

        parameters = {}
        for i in pLookup:
            parameters[i] =  obj.getValue(i)

        session.execute(query, parameters)

    @staticmethod
    def updateWithObjectInfo(session, objectName, parameters, parameterList, query):

        #parameters = {}
        #parameters['id'] = id
        #parameters['thread_id'] = thread_id
        #parameters['text1'] = text1
        #parameters['poster'] = poster
        #parameters['timestamp1'] = timestamp1

        parameterList = "thread_id = %(thread_id)s, text1 = %(text1)s, poster = %(poster)s, timestamp1 = %(timestamp1)s"
        query = """
            UPDATE {objectName} SET
                {parameterList}
                WHERE id = %(id)s
        """.format(objectName=objectName, parameterList=parameterList)
        
        session.execute(query, parameters)

    @staticmethod
    def updateObject(session, obj):

        pLookup = obj.objectPropertyList
        
        parameterList = ', '.join(map(lambda i: "{tag} = %({tag})s".format(tag=i), pLookup))
        query = """
            UPDATE {objectName} SET
                {parameterList}
                WHERE id = %(id)s
        """.format(objectName=obj.objectEntity, parameterList=parameterList)
        
        pLookupWithId = obj.objectPropertyListWithId
        parameters = {}
        for i in pLookupWithId:
            parameters[i] =  obj.getValue(i)

        session.execute(query, parameters)

    @staticmethod
    def deleteWithObjectInfo(session, objectName, id, query):

        query = """
            DELETE FROM {objectName} WHERE id = %(id)s
        """.format(objectName=objectName)
        
        session.execute(query, {'id': id})

    @staticmethod
    def deleteObject(session, obj):

        query = """
            DELETE FROM {objectName} WHERE id = %(id)s
        """.format(objectName=obj.objectEntity)
        
        session.execute(query, {'id': obj.id})

    @staticmethod
    def closeDb(conn):
        conn['session'].shutdown()
        conn['cluster'].shutdown()


