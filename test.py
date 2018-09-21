from forum import forum
from threadConversation import threadConversation
from db import db
#from commonUtility import commonUtility

x = forum()
x.name = "test"
x.creator = "ddsd"


db.executeInsert('proj1.db', x)
print(x.id)
