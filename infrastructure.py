
class infrastructure:

    moduloKey = 3
    shardDbBase = "posts"
    dbPath = "proj1.db"

    @staticmethod
    def getShardKey(ctxData):
        return ctxData % infrastructure.moduloKey
    
    @staticmethod
    def getDb(ctxData):
        return infrastructure.shardDbBase + str(infrastructure.getShardKey(ctxData)) + ".db"

    @staticmethod
    def getDbCommon():
        return infrastructure.dbPath

