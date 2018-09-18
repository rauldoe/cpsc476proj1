import sqlite3

from flask import current_app, g

#from flask.cli import with_appcontext

dbKey = "db"
dbConfigKey = "DATABASE"
schemaFile = "schema.sql"
encoding = "utf8"


def get_db():
    if dbKey not in g:
        g.db = sqlite3.connect(
            current_app.config[dbConfigKey],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop(dbKey, None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource(schemaFile) as f:
        db.executescript(f.read().decode(encoding))