#!flask/bin/python3

import sqlite3

from flask import Flask
from flask import g
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from flask_basicauth import BasicAuth

from db import db
from forum import forum
from forumList import forumList
from cpsc476Auth import cpsc476Auth

Ok = 200
Created = 201
NotFound = 404

GET = "GET"
POST = "POST"

forumsUrl = "/forums"
forumsFromIdUrl = forumsUrl + "/<int:id>"

dbPath = "test.db"

app = Flask(__name__)

basic_auth = cpsc476Auth(app)

@app.route(forumsUrl, methods=[GET])
def forumsGet():

    ilist = forumList()

    query = "SELECT id, name, creator FROM {table};".format(table="forums")
    conn = db.initDb(dbPath)
    dataList = db.executeReturnList(conn, query)
    for i in dataList:
        ilist.appendItem(i["id"], i["name"], i["creator"])

    db.closeDb(conn)

    return make_response(ilist.serialize(), Ok)

@app.route(forumsUrl, methods=[POST])
def forumsPost():

    obj = forum.deserialize(request.json)
    return make_response(obj.serializeJson(), Created)

@app.route(forumsFromIdUrl, methods=[GET])
@basic_auth.required
def forumsFromIdGet(forum_id):

    ilist = forumList.test()
    subList = ilist.find(forum_id)

    subList.mList[0].creator = basic_auth.username

    return make_response(subList.serialize(), Ok)

@app.errorhandler(NotFound)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), NotFound)

if __name__ == '__main__':
    app.run(debug=True)
