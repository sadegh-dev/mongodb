import pymongo


# Connect to Monog DataBase

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

mycol = mydb["customers"]


# find one data

#data_ = mycol.find_one()
#print(data_)


# find all data

data_ = mycol.find()
for x in data_:
    print(x)

