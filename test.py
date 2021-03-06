import pymongo


# Connect to Mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Connect to Database [create DataBase]

db_name = "dbtest"
mydb = myclient[db_name]


# Connect to the Collection [create Collection]

collection_name = "customers"
mycol = mydb[collection_name]


# find multiple data

myquery = { 
    '$or':[
        {'name': 'charlie'} ,
        {'name': 'Michael'}
    ]
}

"""
{'name': 'charlie', 'address': 'berlin, street 4'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Viola', 'address': 'Sideway 1633'}
{'name': 'janet', 'address': 'hamburg, street 48'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Susan', 'address': 'One way 98'}
"""




data_ = mycol.find(myquery,{'_id':0})
#print(data_)


data_ = mycol.aggregate([{
    '$group' : {
        '_id' : "$name",
        'numbers' : {
            '$sum' : 1
        }
    }
}])


# Access All Documents

for x in data_ :
    print(x)


