
import sqlite3

from flask import Flask
from flask import g
from flask import request
from flask import jsonify
from flask import make_response
from forum import forum
from forumList import forumList

Ok = 200
Created = 201

GET = "GET"
POST = "POST"

forumsUrl = "/forums"
forumsFromIdUrl = forumsUrl + "/<int:id>"

app = Flask(__name__)

@app.route(forumsUrl, methods=[GET])
def forumsGet():

    list = forumList()

    list.appendItem(1, "name1", "creator1")
    list.appendItem(2, "name2", "creator2")
    list.appendItem(3, "name3", "creator3")

    return make_response(list.serialize(), Ok)

@app.route(forumsUrl, methods=[POST])
def forumsPost():
    return make_response(forum.deserialize(request.json).serializeJson(), Created)

@app.route(forumsFromIdUrl, methods=[GET])
def forumsFromIdGet(id):

    list = forumList()

    list.appendItem(1, "name1", "creator1")
    list.appendItem(2, "name2", "creator2")
    list.appendItem(3, "name3", "creator3")

    return make_response(list.find(1).serialize(), Ok)