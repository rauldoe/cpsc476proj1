import sqlite3

#executeSchema("test.db", "init.sql")
def executeSchema(dbPath, schemaPath):

    conn = initDb(dbPath)
    schema = loadFile(schemaPath)
    executeScript(conn, schema)
    closeDb(conn)

#support functions
def initDb(dbPath):
    conn = sqlite3.connect(
            dbPath,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    return conn

def closeDb(conn):
    conn.commit()
    conn.close()

def execute(conn, query):
    cur = conn.cursor()
    cur.execute(query)

def executeScript(conn, queryFromScript):
    cur = conn.cursor()
    cur.executescript(queryFromScript)

def loadFile(filePath):
    data = ""

    with open(filePath, 'r') as filePtr:
        data = filePtr.read().replace('\n', '')

    return data


