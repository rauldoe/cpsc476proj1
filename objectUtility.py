from commonUtility import commonUtility

class objectUtility:

    #support functions
    @staticmethod
    def getExistQuery(obj, propertyTagList):
        pLookup = obj.objectPropertyListWithId
        whereClause = ' AND '.join(map(lambda i: "{col} = '{val}'".format(col=i, val=commonUtility.getValuefromKeyValueString(pLookup, i)), propertyTagList))
        return "SELECT 1 FROM {entity} WHERE {whereClause};".format(entity=obj.objectEntity, whereClause=whereClause)
    
    @staticmethod
    def getSelectQuery(objType, whereList):
        obj = objType()
        pLookup = obj.objectPropertyListWithId
        columnList = ', '.join(map(lambda i: i, pLookup))
        if len(whereList) > 0:
            whereClause = " WHERE {listString}".format(listString=' AND '.join(map(lambda i: "{col} = '{val}'".format(col=i, val=whereList[i]), whereList)))
        else:
            whereClause = ""

        return "SELECT {columnList} FROM {entity}{whereClause};".format(columnList=columnList, entity=obj.objectEntity, whereClause=whereClause)
