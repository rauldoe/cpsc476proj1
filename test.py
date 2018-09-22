import json

from flask import jsonify

from forum import forum
from threadConversation import threadConversation
from db import db
from post import post

from commonUtility import commonUtility
from appUtility import appUtility

dbPath = 'proj1.db'

x = forum()
x.name = "test"
x.creator = "ddsd"

xlist = [x]

#db.executeInsert('proj1.db', x)
#print(json.dumps([i.serializeItem() for i in xlist]))

y = post()
y.thread_id = 90
y.text1 = "weereredsf"
#print(db.getExistQuery(x, ["name", "creator"]))

#print(db.getSelectQuery(forum, {"name":"testerdsfds", "creator":"maymay"}))
#print(db.getSelectQuery(post, {"thread_id":7878, "title":"223k432jl"}))
#print(db.getSelectQuery(post, {}))
whereList = {}
whereList = {"poster":"jack"}
olist = appUtility.loadList(dbPath, post, whereList)

propFunc1 = lambda obj, i:print(i+":"+str(obj.getValue(i)))
#olist.processPerProperty(propFunc1, appUtility.emptyFunc, appUtility.emptyFunc)

y = post()
y.id = 8838
y.thread_id = 90
y.text = "weereredsf"
db.executeUpdate(dbPath, y, ["id", "thread_id"])