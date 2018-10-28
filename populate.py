import sqlite3
import uuid

sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
sqlite3.register_adapter(uuid.UUID, lambda u: buffer(u.bytes_le))

conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES)

c = conn.cursor()
c.execute('CREATE TABLE test (guid GUID PRIMARY KEY, name TEXT)')

data = (uuid.uuid4(), 'foo')
print 'Input Data:', data
c.execute('INSERT INTO test VALUES (?,?)', data)

c.execute('SELECT * FROM test')
print 'Result Data:', c.fetchone()