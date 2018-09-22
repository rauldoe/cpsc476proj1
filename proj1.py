#!flask/bin/python3

import sqlite3
import datetime

from flask import Flask
from flask import g
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from flask import abort

from flask_basicauth import BasicAuth

from db import db
from forum import forum
from threadConversation import threadConversation
from post import post
from cpsc476Auth import cpsc476Auth
from httpUtility import httpUtility
from commonUtility import commonUtility
from objectBase import objectBase
from appUtility import appUtility
from user import user

forumsUrl = "/forums"
forumsFromForumIdUrl = forumsUrl + "/<int:forum_id>"
forumsFromForumIdThreadIdUrl = forumsFromForumIdUrl + "/<int:thread_id>"

usersUrl = "/users"
usersByUsernameUrl = usersUrl + "/<string:username>"

dbPath = commonUtility.dbPath

app = Flask(__name__)

basic_auth = cpsc476Auth(app)

#def __init__(self):
#    self.basic_auth.dbPath = dbPath

@app.route(forumsUrl, methods=[httpUtility.GET])
def getForums():

    whereList = {}
    ilist = appUtility.loadList(dbPath, forum, whereList)
    response = make_response(ilist.serialize(), httpUtility.Ok)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route(forumsUrl, methods=[httpUtility.POST])
@basic_auth.required
def createForum():

    obj = objectBase.deserializeObject(request.json, forum)
    obj.creator = basic_auth.username

    isPassed = appUtility.ifExistDoError(dbPath, obj, ["name"], httpUtility.Conflict)
    if not isPassed:
        return
    
    db.executeInsert(dbPath, obj)
    return make_response(obj.serializeJson(), httpUtility.Created)

@app.route(forumsFromForumIdUrl, methods=[httpUtility.GET])
def getThreadsByForum(forum_id):

    whereList = {"forum_id":forum_id}
    ilist = appUtility.loadList(dbPath, threadConversation, whereList)

    response = make_response(ilist.serialize(), httpUtility.Ok)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route(forumsFromForumIdUrl, methods=[httpUtility.POST])
@basic_auth.required
def createThread(forum_id):

    obj = objectBase.deserializeObject(request.json, threadConversation)
    obj.forum_id = forum_id
    obj.author = basic_auth.username
    obj.timestamp = datetime.datetime.now()

    isPassed = appUtility.ifNotExistDoError(dbPath, obj, ["forum_id"], httpUtility.NotFound)
    if not isPassed:
        return

    obj = db.executeInsert(dbPath, obj)

    response = make_response(obj.serializeJson(), httpUtility.Created)

    response.headers["Location"] = "{url}/{forum_id}/{thread_id}".format(url=forumsUrl, forum_id=obj.forum_id, thread_id=obj.id)

    return response

@app.route(forumsFromForumIdThreadIdUrl, methods=[httpUtility.GET])
def getPostsByThread(forum_id, thread_id):

    checkObj = threadConversation()
    checkObj.id = thread_id
    checkObj.forum_id = forum_id

    isPassed = appUtility.ifNotExistDoError(dbPath, checkObj, ["id", "forum_id"], httpUtility.NotFound)
    if not isPassed:
        return

    whereList = {"thread_id":thread_id}
    ilist = appUtility.loadList(dbPath, post, whereList)

    response = make_response(ilist.serialize(), httpUtility.Ok)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route(forumsFromForumIdThreadIdUrl, methods=[httpUtility.POST])
@basic_auth.required
def createPost(forum_id, thread_id):

    checkObj = threadConversation()
    checkObj.id = thread_id
    checkObj.forum_id = forum_id

    isPassed = appUtility.ifNotExistDoError(dbPath, checkObj, ["id", "forum_id"], httpUtility.NotFound)
    if not isPassed:
        return

    obj = objectBase.deserializeObject(request.json, post)
    obj.thread_id = thread_id
    obj.poster = basic_auth.username
    obj.timestamp = datetime.datetime.now()
    obj = db.executeInsert(dbPath, obj)

    response = make_response(obj.serializeJson(), httpUtility.Created)

    return response

@app.route(usersUrl, methods=[httpUtility.POST])
def createUser():

    obj = objectBase.deserializeObject(request.json, user)

    isPassed = appUtility.ifExistDoError(dbPath, obj, ["username"], httpUtility.Conflict)
    if not isPassed:
        return

    obj = db.executeInsert(dbPath, obj)

    response = make_response("", httpUtility.Created)

    return response

@app.route(usersByUsernameUrl, methods=[httpUtility.PUT])
@basic_auth.required
def changeUserPassword(username):

    obj = objectBase.deserializeObject(request.json, user)
    obj.username = username

    isPassed = appUtility.ifNotExistDoError(dbPath, obj, ["username"], httpUtility.NotFound)
    if not isPassed:
        return

    if obj.username != basic_auth.username:
        abort(httpUtility.Conflict)

    obj = db.executeUpdate(dbPath, obj, ["username"])

    response = make_response("", httpUtility.Ok)

    return response

@app.errorhandler(httpUtility.NotFound)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), httpUtility.NotFound)

if __name__ == '__main__':
    app.run(debug=True)
