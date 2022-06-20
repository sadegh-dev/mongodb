import pymongo


# Connect to Monog DataBase

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

mycol = mydb["customers"]


# List of Collections

collections_ = mydb.list_collection_names()
print(collections_)

