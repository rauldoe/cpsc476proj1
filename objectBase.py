
from flask import jsonify

class objectBase:
    _idTag = "id"
    _objectName = "objectName"
    _objectLookup = {}

    def __init__(self, id):
        self.id = id

    @property
    def objectLookup(self):
        return self._objectLookup

    @property
    def objectPropertyList(self):
        pLookup = {}
        for k, v in self._objectLookup.items():
            if not self.isInstrinsic(k):
                pLookup[k] = v

        return pLookup

    #id
    @property
    def id(self):
        return self._objectLookup[self._idTag]

    @id.setter
    def id(self, value):
        self._objectLookup[self._idTag] = value

    #objectName
    @property
    def objectName(self):
        return self._objectLookup[self._objectName]

    @objectName.setter
    def objectName(self, value):
        self._objectLookup[self._objectName] = value

    #functions
    def isInstrinsic(self, tag):
        return ((tag == self._idTag)  or (tag == self._objectName))

    def serialize(self):
        return self._objectLookup
    
    def serializeJson(self):
        return jsonify(self.serialize())