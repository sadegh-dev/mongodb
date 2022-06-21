import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

collection_name = "customers"
mycol = mydb[collection_name]


# Insert [One] Document (record)

data_ = {
    "name" : "janet" ,
    "address" : "hamburg, street 48"
}

id_insert_data = mycol.insert_one(data_)
print(id_insert_data)


# insert data with id_
# Refer to the educational source ...
