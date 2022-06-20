import pymongo


# Connect to Monog DataBase

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

mycol = mydb["customers"]


# Insert [One] Document (record)

data_ = {
    "name" : "charlie" ,
    "address" : "berlin, street 4"
}

id_insert_data = mycol.insert_one(data_)
print(id_insert_data)