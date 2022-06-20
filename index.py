import pymongo


# Connect to Monog DataBase

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Collection (Database) [create collection]

collection_name = "dbtest"
mydb = myclient[collection_name]


# List of Collections

collections = myclient.list_database_names()
print(collections)





