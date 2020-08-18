from pymongo import MongoClient

class MongoContext(object):
    
    def __init__(self, connectionString):
        self.__database = MongoClient(connectionString)

    def GetCollection(self, dbName):
        try:
            return self.__database[dbName]
                     
        except Exception as e:
            print(F"Exception at MongoDB context: {str(e)}")

