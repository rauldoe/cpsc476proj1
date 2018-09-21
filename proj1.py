#!flask/bin/python3

import sqlite3
import datetime

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
from threadConversation import threadConversation
from cpsc476Auth import cpsc476Auth
from httpUtility import httpUtility
from commonUtility import commonUtility

forumsUrl = "/forums"
forumsFromForumIdUrl = forumsUrl + "/<int:forum_id>"
forumsFromForumIdThreadIdUrl = forumsFromForumIdUrl + "/<int:thread_id>"

usersUrl = "/users"
usersByUsernameUrl = usersUrl + "/<string:username>"

dbPath = "proj1.db"

app = Flask(__name__)

basic_auth = cpsc476Auth(app)

@app.route(forumsUrl, methods=[httpUtility.GET])
def getForums():

    ilist = forumList.loadList(dbPath)

    return make_response(ilist.serialize(), httpUtility.Ok)

@app.route(forumsUrl, methods=[httpUtility.POST])
@basic_auth.required
def createForum():

    obj = forum.deserialize(request.json)
    obj.creator = basic_auth.username

    #obj.name
    #SELECT name from forums WHERE name = {obj.name}
    query = "INSERT INTO forums(name, creator) "\
        + "VALUES ('{name}',  '{creator}');".format(name=obj.name, creator=obj.creator)
    conn = db.initDb(dbPath)
    id = db.executeReturnId(conn, query)
    db.closeDb(conn)

    obj.id = id

    response = make_response(obj.serializeJson(), httpUtility.Created)

    response.headers["Location"] = "{url}/{forum_id}".format(url=forumsUrl, forum_id=obj.id)

    return response

@app.route(forumsFromForumIdUrl, methods=[httpUtility.GET])
def getThreadsByForum(forum_id):

    ilist = forumList.test()
    subList = ilist.find(forum_id)

    return make_response(subList.serialize(), httpUtility.Ok)

@app.route(forumsFromForumIdUrl, methods=[httpUtility.POST])
@basic_auth.required
def createThread(forum_id):

    query = "SELECT 1 FROM forums WHERE id = '{forum_id}';".format(forum_id=forum_id)
    isPassed = commonUtility.ifNotExistDoError(dbPath, query, httpUtility.NotFound)
    if not isPassed:
        return

    id = 0
    obj = threadConversation.deserialize(request.json)
    obj.forum_id = forum_id
    obj.author = basic_auth.username
    obj.timestamp1 = datetime.datetime.now()

    #INSERT INTO threads(forum_id, title, text1, author, timestamp1) VALUES (1, 'first thread - first forum', 'hey this is great', 'paul', date('now'));
    query = "INSERT INTO threads(forum_id, title, text1, author, timestamp1) "\
        + "VALUES ('{forum_id}',  '{title}', '{text}', '{author}', '{timestamp}');".format(forum_id=obj.forum_id, title=obj.title, text=obj.text1, author=obj.author, timestamp=obj.timestamp1)
    conn = db.initDb(dbPath)
    id = db.executeReturnId(conn, query)
    db.closeDb(conn)

    obj.id = id

    response = make_response(obj.serializeJson(), httpUtility.Created)

    response.headers["Location"] = "{url}/{forum_id}/{thread_id}".format(url=forumsUrl, forum_id=forum_id, thread_id=id)

    return response

@app.route(forumsFromForumIdThreadIdUrl, methods=[httpUtility.GET])
def getPostsByThread(forum_id, thread_id):

    ilist = forumList.test()
    subList = ilist.find(forum_id)

    subList.mList[0].creator = basic_auth.username

    return make_response(subList.serialize(), httpUtility.Ok)

@app.route(forumsFromForumIdThreadIdUrl, methods=[httpUtility.POST])
@basic_auth.required
def createPost(forum_id, thread_id):

    #basic_auth.username
    obj = forum.deserialize(request.json)
    obj.thread_id=thread_id
    obj.poster = basic_auth.username
    obj.timestamp1 = datetime.datetime.now()

    query = "INSERT INTO posts(thread_id, text1, poster, timestamp1) "\
        + "VALUES ('{thread_id}',  '{text}', '{poster}', '{timestamp}');".format(thread_id=obj.thread_id, text=obj.text1, poster=obj.poster, timestamp=obj.timestamp1)
    conn = db.initDb(dbPath)
    forum_id=obj.forum_id
    thread_id = db.executeReturnId(conn, query)
    db.closeDb(conn)

    obj.id = thread_id

    response = make_response(obj.serializeJson(), httpUtility.Created)

    response.headers["Location"] = "{url}/{forum_id}/{thread_id}".format(url=forumsUrl, forum_id=forum_id, thread_id=thread_id)

    return response


@app.route(usersUrl, methods=[httpUtility.POST])
def createUser():

    ilist = forumList()

    query = "SELECT id, name, creator FROM {table};".format(table="forums")
    conn = db.initDb(dbPath)
    dataList = db.executeReturnList(conn, query)
    for i in dataList:
        ilist.appendItem(i["id"], i["name"], i["creator"])

    db.closeDb(conn)

    return make_response(ilist.serialize(), httpUtility.Ok)

@app.route(usersByUsernameUrl, methods=[httpUtility.PUT])
@basic_auth.required
def changeUserPassword(username):

    ilist = forumList()

    query = "SELECT id, name, creator FROM {table};".format(table="forums")
    conn = db.initDb(dbPath)
    dataList = db.executeReturnList(conn, query)
    for i in dataList:
        ilist.appendItem(i["id"], i["name"], i["creator"])

    db.closeDb(conn)

    return make_response(ilist.serialize(), httpUtility.Ok)

@app.errorhandler(httpUtility.NotFound)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), httpUtility.NotFound)

if __name__ == '__main__':
    app.run(debug=True)
