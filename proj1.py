
import sqlite3

from flask import Flask, jsonify
from flask import g
from forum import forum

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/forums")
def forums():

    forumList = []

    f = forum()

    f.id = 290
    f.name = "paul"
    f.creator = "testor"


    forumList.append(f)

    f = forum()

    f.id = 29022
    f.name = "paulddd"
    f.creator = "testorss"

    forumList.append(f)

    return jsonify([i.serialize() for i in forumList])

DATABASE = "database.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if v else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()