
from commonUtility import commonUtility
from cassandra.cluster import Cluster

class cql:

    @staticmethod
    def initDb(keyspace):
        cluster = Cluster()
        session = cluster.connect()

        #keyspace = "proj3"
        session.set_keyspace(keyspace)

        return {'cluster': cluster, 'session': session}

    @staticmethod
    def retrieveList(session, objectName):
        return session.execute("SELECT * FROM {objectName};".format(objectName=objectName))
    
    @staticmethod
    def insertObject(session, objectName, parameters, parameterTagList, parameterIdList, query):

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
    def updateObject(session, objectName, parameters, parameterList, query):

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
    def deleteObject(session, objectName, id, query):

        query = """
            DELETE FROM {objectName} WHERE id = %(id)s
        """.format(objectName=objectName, id=id)
        
        session.execute(query, {'id': id})

    @staticmethod
    def closeDb(conn):
        conn['session'].shutdown()
        conn['cluster'].shutdown()


