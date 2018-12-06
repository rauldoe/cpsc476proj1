from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import uuid
import datetime

cluster = Cluster()
session = cluster.connect()

session.set_keyspace('mykey')
session.row_factory = dict_factory

session.execute(
    """
    INSERT INTO posts (id, thread_id, text1, poster, timestamp1)
    VALUES (%(id)s, %(thread_id)s, %(text1)s, %(poster)s, %(timestamp1)s)
    """,
    {'id': uuid.uuid4(), 'thread_id': 333, 'text1':  'dfdsfs', 'poster': 'sdsdsds', 'timestamp1': datetime.datetime.now()}
)