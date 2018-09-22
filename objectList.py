import json

from objectBase import objectBase

class objectList:

    def __init__(self, objectType):
        obj = objectType()
        self.objectType = obj.objectType
        self.objectName = obj.objectName
        self.mList = []

    def append(self, item):
        self.mList.append(item)

    def serialize(self):
        return json.dumps([i.serializeItem() for i in self.mList])

    def find(self, id):
        subList = objectList(self.objectType)
        for i in iter(self.mList):
            if i.id == id:
                subList.append(i)
        return subList
    
    def process(self, listFunc, preFunc, postFunc):
        preFunc()
        for i in self.mList:
            listFunc(i)
        postFunc()

    def processPerProperty(self, propFunc, preFunc, postFunc):
        listFunc = lambda i: i.process(propFunc)
        self.process(listFunc, preFunc, postFunc)
