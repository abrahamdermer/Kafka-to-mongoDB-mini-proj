import pymongo


class Insertdb:
    def __init__(self):
        self.address = "mongodb://localhost:27000/"
        self.db = "news"

    def insert(self,col,dic):
        myclient = pymongo.MongoClient(self.address)
        mydb = myclient[self.db]
        mycol = mydb[col]
        mycol.insert_one(dic)
        myclient.close()