
class commonUtility:

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

    @staticmethod
    def loadFile(filePath):
        data = ""

        with open(filePath, 'r') as filePtr:
            data = filePtr.read().replace('\n', '')

        return data

    @staticmethod
    def loadFileWithDelimiter(filePath, delim):
        data = []

        with open(filePath, 'r') as filePtr:

            query = ""
            workData = []

            for inputData in filePtr:

                inputData = inputData.rstrip(None)
                if (not inputData.isspace()):
                    workData.append(inputData)
                if (inputData.find(delim) >= 0):
                    query = ' '.join(map(lambda i: i, workData))
                    print('found ' + query)
                    data.append(query.lstrip(None))
                    workData = []
                    query = ""
            #for 
        #with

        return data