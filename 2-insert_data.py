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

#id_insert_data = mycol.insert_one(data_)
#print(id_insert_data)


# Insert [more] Document

data_ = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

ids_insert_data = mycol.insert_many(data_)
print(ids_insert_data)


# insert data with id_
# Refer to the educational source ...

