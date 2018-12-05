
from infrastructure import infrastructure
from db import db
from populate_post import populate_post
from cql import cql

class create_test_data:

    @staticmethod
    def init():
        dbPath = infrastructure.getDbCommon()
        db.executeScriptPath(dbPath, "init.sql")
        db.executeScriptPath(dbPath, "populate.sql")

        initPost = "init_post.sql"

        dbPath = infrastructure.getDb(1)
        db.executeScriptPath(dbPath, initPost)

        dbPath = infrastructure.getDb(2)
        db.executeScriptPath(dbPath, initPost)

        dbPath = infrastructure.getDb(3)
        db.executeScriptPath(dbPath, initPost)

        populate_post.populate()

    @staticmethod
    def initCql():
        dbPath = infrastructure.getDbCommon()
        db.executeScriptPath(dbPath, "init.sql")
        db.executeScriptPath(dbPath, "populate.sql")

        keyspace = infrastructure.getKeyspace()
        conn = cql.initDb(keyspace)
        session = conn['session']

        cql.executeScriptPath(session, "init_post1.cql")
        cql.executeScriptPath(session, "populate_post1.cql")
        
        cql.closeDb(conn)
