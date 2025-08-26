import pymongo


class DAL:

    def __init__(self):
        self.addres = "mongodb://localhost:27000/"
        self.db = "news"
            

    def get_all_tata_from_colume(self,col):
        myclient = pymongo.MongoClient(self.addres)
        mydb = myclient[self.db]
        mycol = mydb[col]
        rec = mycol.find({},{'_id':0}).to_list()
        return rec


