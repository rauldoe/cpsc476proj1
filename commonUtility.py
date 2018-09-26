
class commonUtility:

    dbPath = "proj1.db"

    @staticmethod
    def getValuefromKeyValueString(dict, key):
        if key is None:
            return ""
        elif dict[key] is None:
            return ""
        else:
            return dict[key]

    @staticmethod
    def dictGetSafe(dict, key):
        if key in dict:
            return dict[key]
        else:
            return None
