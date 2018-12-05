
from cql import cql

objectName = "posts"
keyspace = "proj3"
conn = cql.initDb(keyspace)

#dataList = cql.retrieveList(conn['session'], objectName)

id = 4
thread_id = 42
text1 = "my new text4"
poster = "new new poster"
timestamp1 = "2018-11-30"

new_thread_id = 33
new_text1 = "not so new text1"

parameters = {}
parameters['id'] = id
parameters['thread_id'] = thread_id
parameters['text1'] = text1
parameters['poster'] = poster
parameters['timestamp1'] = timestamp1

parameterTagList = "id, thread_id, text1, poster, timestamp1"
parameterIdList = "%(id)s, %(thread_id)s, %(text1)s, %(poster)s, %(timestamp1)s"
query = ""

cql.insertWithObjectInfo(conn['session'], objectName, parameters, parameterTagList, parameterIdList, query)

dataList = cql.executeReturnList(conn['session'], objectName)

print("Posts Table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

parameters = {}
parameters['id'] = id
parameters['thread_id'] = new_thread_id
parameters['text1'] = new_text1
parameters['poster'] = poster
parameters['timestamp1'] = timestamp1

parameterList = "thread_id = %(thread_id)s, text1 = %(text1)s, poster = %(poster)s, timestamp1 = %(timestamp1)s"
query = ""

cql.updateWithObjectInfo(conn['session'], objectName, parameters, parameterList, query)

dataList = cql.executeReturnList(conn['session'], objectName)

print("Posts Table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

idToDelete = 4
query = ""
cql.deleteWithObjectInfo(conn['session'], objectName, idToDelete, query)

dataList = cql.executeReturnList(conn['session'], objectName)

print("Posts Table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

cql.closeDb(conn)