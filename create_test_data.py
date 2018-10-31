
from infrastructure import infrastructure
from db import db
from populate_post import populate_post

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

