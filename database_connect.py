import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbstest"
mydb = myclient[db_name]

