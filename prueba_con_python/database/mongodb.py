from database.db import Database
import pymongo


class MongoConection(Database):
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["r_python"]

    def insert(self, data, collection_name):
        mycol = self.mydb[collection_name]
        mycol.insert_many(data)
