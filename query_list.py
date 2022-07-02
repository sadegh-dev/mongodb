import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

collection_name = "customers"
mycol = mydb[collection_name]


# Query statements ###############
##################################

# 1 ##########################
myquery = { 
    '$or':[
        {'name': 'charlie'} ,
        {'name': 'Sandy'}
    ]

}

# 2 ##########################




##################################
##################################

data_ = mycol.find(myquery,{'_id':0})
print(data_)

for x in data_ :
    print(x)


