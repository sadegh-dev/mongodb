import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# List of Databases

databases = myclient.list_database_names()
print(databases)





