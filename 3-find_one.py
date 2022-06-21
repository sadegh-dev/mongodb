import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

collection_name = "customers"
mycol = mydb[collection_name]


# find one data

data_ = mycol.find_one()
print(data_)


# can Return Some Fields
# Check Resource:
# https://www.w3schools.com/python/python_mongodb_find.asp

