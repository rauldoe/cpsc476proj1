
import sqlite3

from flask import Flask
from flask import g
from flask import request
from flask import jsonify
from forum import forum
from forumList import forumList

app = Flask(__name__)

@app.route("/forums")
def forums():

    list = forumList()

    list.appendItem(1, "name1", "creator1")
    list.appendItem(2, "name2", "creator2")
    list.appendItem(3, "name3", "creator3")

    return list.serialize()

@app.route("/forums", methods=["POST"])
def forumsPost():
    #return forum(0, "test", "").serialize(), 201
    return jsonify(forum.deserialize(request.json).serialize()), 201
