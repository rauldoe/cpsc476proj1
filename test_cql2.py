
from cql import cql
from post1 import post1

objectName = "post1s"
keyspace = "proj3"
conn = cql.initDb(keyspace)

id = 4
thread_id = 42
text1 = "my new text4"
poster = "new new poster"
timestamp1 = "2018-11-30"

new_thread_id = 33
new_text1 = "not so new text1"


obj = post1()
obj.id = id
obj.thread_id = thread_id
obj.text1 = text1
obj.poster = poster
obj.timestamp1 = timestamp1

cql.insertObject(conn['session'], obj)

dataList = cql.executeReturnObjectList(conn['session'], obj)

print("Post table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

obj = post1()
obj.id = id
obj.thread_id = new_thread_id
obj.text1 = new_text1
obj.poster = poster
obj.timestamp1 = timestamp1

cql.updateObject(conn['session'], obj)

dataList = cql.executeReturnObjectList(conn['session'], obj)

print("Post table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

cql.deleteObject(conn['session'], obj)

dataList = cql.executeReturnObjectList(conn['session'], obj)

print("Post table")
for i in dataList:
    print(str(i.id) + ", " + i.text1 + ", " + i.poster + ", " + str(i.thread_id))

cql.closeDb(conn)


