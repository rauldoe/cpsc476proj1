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
from Auth import Auth
from objectBase import objectBase
from helper import helper
from user import user

forumsUrl = "/forums"
forumsFromForumIdUrl = forumsUrl + "/<int:forum_id>"
forumsFromForumIdThreadIdUrl = forumsFromForumIdUrl + "/<int:thread_id>"

usersUrl = "/users"
usersByUsernameUrl = usersUrl + "/<string:username>"

dbPath = "proj1.db"

app = Flask(__name__)

basic_auth = Auth(app)

@app.route(forumsUrl, methods=['GET'])
def getForums():

    whereList = {}
    ilist = helper.getList(dbPath, forum, whereList)
    response = make_response(ilist.serialize(), 200)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route(forumsUrl, methods=['POST'])
@basic_auth.required
def createForum():

    obj = objectBase.deserializeObject(request.json, forum)
    obj.creator = basic_auth.username

    isPassed = helper.ifExistDoError(dbPath, obj, ["name"], 409)
    if not isPassed:
        return

    db.executeInsert(dbPath, obj)
    return make_response(obj.serializeJson(), 201)

@app.route(forumsFromForumIdUrl, methods=['GET'])
def getThreadsByForum(forum_id):

    whereList = {"forum_id":forum_id}
    ilist = helper.getList(dbPath, threadConversation, whereList)

    response = make_response(ilist.serialize(), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route(forumsFromForumIdUrl, methods=['POST'])
@basic_auth.required
def createThread(forum_id):

    obj = objectBase.deserializeObject(request.json, threadConversation)
    obj.forum_id = forum_id
    obj.author = basic_auth.username
    obj.timestamp = datetime.datetime.now()

    isPassed = helper.ifNotExistDoError(dbPath, obj, ["forum_id"], 404)
    if not isPassed:
        return

    obj = db.executeInsert(dbPath, obj)

    response = make_response(obj.serializeJson(), 201)

    response.headers["Location"] = "{url}/{forum_id}/{thread_id}".format(url=forumsUrl, forum_id=obj.forum_id, thread_id=obj.id)

    return response

@app.route(forumsFromForumIdThreadIdUrl, methods=['GET'])
def getPostsByThread(forum_id, thread_id):

    checkObj = threadConversation()
    checkObj.id = thread_id
    checkObj.forum_id = forum_id

    isPassed = helper.ifNotExistDoError(dbPath, checkObj, ["id", "forum_id"], 404)
    if not isPassed:
        return

    whereList = {"thread_id":thread_id}
    ilist = helper.getList(dbPath, post, whereList)

    response = make_response(ilist.serialize(), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route(forumsFromForumIdThreadIdUrl, methods=['POST'])
@basic_auth.required
def createPost(forum_id, thread_id):

    checkObj = threadConversation()
    checkObj.id = thread_id
    checkObj.forum_id = forum_id

    isPassed = helper.ifNotExistDoError(dbPath, checkObj, ["id", "forum_id"], 404)
    if not isPassed:
        return

    obj = objectBase.deserializeObject(request.json, post)
    obj.thread_id = thread_id
    obj.poster = basic_auth.username
    obj.timestamp = datetime.datetime.now()
    obj = db.executeInsert(dbPath, obj)

    response = make_response(obj.serializeJson(), 201)

    return response

@app.route(usersUrl, methods=['POST'])
def createUser():

    obj = objectBase.deserializeObject(request.json, user)

    isPassed = helper.ifExistDoError(dbPath, obj, ["username"], 409)
    if not isPassed:
        return

    obj = db.executeInsert(dbPath, obj)

    response = make_response("", 201)

    return response

@app.route(usersByUsernameUrl, methods=['PUT'])
@basic_auth.required
def changeUserPassword(username):

    obj = objectBase.deserializeObject(request.json, user)
    obj.username = username

    isPassed = helper.ifNotExistDoError(dbPath, obj, ["username"], 404)
    if not isPassed:
        return

    if obj.username != basic_auth.username:
        abort(409)

    obj = db.executeUpdate(dbPath, obj, ["username"])

    response = make_response("", 200)

    return response

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
