
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

keyspace = "proj3"
session.set_keyspace(keyspace)

#INSERT INTO proj3.posts(id, thread_id, text1, poster, timestamp1)
#    VALUES(3, 3, 'text3', 'poster3', '2011-02-05');

dataList = session.execute("SELECT * FROM posts;")

#for i in dataList:
#    print(i.text1)

id = 4
thread_id = 42
text1 = "my new text4"
poster = "new new poster"
timestamp1 = "2018-11-30"

new_thread_id = 33
new_text1 = "not so new text1"

query = """
    INSERT INTO posts (id, thread_id, text1, poster, timestamp1)
    VALUES (%(id)s, %(thread_id)s, %(text1)s, %(poster)s, %(timestamp1)s)
    """
session.execute(
    """
    INSERT INTO posts (id, thread_id, text1, poster, timestamp1)
    VALUES (%(id)s, %(thread_id)s, %(text1)s, %(poster)s, %(timestamp1)s)
    """,
    {'id': id, 'thread_id': thread_id, 'text1':  text1, 'poster': poster, 'timestamp1': timestamp1}
)

dataList = session.execute("SELECT * FROM posts;")

for i in dataList:
    print(i.text1)

session.execute(
    """
    UPDATE posts SET
        thread_id = %(new_thread_id)s,
        text1     = %(new_text1)s
        WHERE id = %(id)s
    """,
    {'id': id, 'new_thread_id': new_thread_id, 'new_text1': new_text1}
)

dataList = session.execute("SELECT * FROM posts;")

for i in dataList:
    print(i.text1)

session.execute(
    """
    DELETE FROM posts WHERE id = %(id)s
    """,
    {'id': id}
)