import sqlite3
import uuid
import pprint

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
sqlite3.register_adapter(uuid.UUID, lambda u: u.bytes_le)

conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES)
conn.row_factory = make_dicts

c = conn.cursor()
#c.execute('CREATE TABLE test (guid GUID PRIMARY KEY, name TEXT)')

data = (uuid.uuid4(), 'foo')
#pprint.pprint(data)
#c.execute('INSERT INTO test VALUES (?,?)', data)



c.execute('''
        INSERT INTO test(guid, name) 
        VALUES (?, ?)
    '''
    , (uuid.UUID('7005d0e0-f25b-45f9-897d-bae151fddaff'), 'user'))
conn.commit()

#c.execute('SELECT * FROM test')
#pprint.pprint('Result Data:' +  str(c.fetchone()))

c.close()
conn.close()