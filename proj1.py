from flask import Flask, request, jsonify

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

