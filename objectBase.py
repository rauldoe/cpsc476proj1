
from flask import jsonify

from commonUtility import commonUtility

class objectBase:
    _id_tag = "id"
    _objectName_tag = "objectName"

    def __init__(self):
        self._objectLookup = {}
        self._objectLookup[self._id_tag] = None
        self._objectLookup[self._objectName_tag] = "{oname}s".format(oname=self.__class__.__name__)
        self._objectType = self.__class__
        self.id = None

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
        return self._objectLookup[self._id_tag]

    @id.setter
    def id(self, value):
        self._objectLookup[self._id_tag] = value

    #objectName
    @property
    def objectName(self):
        return self._objectLookup[self._objectName_tag]

    @objectName.setter
    def objectName(self, value):
        self._objectLookup[self._objectName_tag] = value

    #functions
    def setValue(self, tag, value):
        self._objectLookup[tag] = value

    def isInstrinsic(self, tag):
        return ((tag == self._id_tag)  or (tag == self._objectName_tag))

    def serialize(self):
        return self._objectLookup
    
    def serializeJson(self):
        return jsonify(self.serialize())
    
    @staticmethod
    def deserializeObject(jsonObj, objectType):

        obj = objectType()

        pLookup = obj.objectPropertyList

        for k in pLookup.keys():
            obj.setValue(k, commonUtility.dictGetSafe(jsonObj, k))

        return obj