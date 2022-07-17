import pymongo
client = pymongo.MongoClient("mongodb+srv://Ramaradhya:Darshan2022@cluster0.m8zah.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Ramaradhya",
    "email" : "ramaradhyabe@gmail.com",
    "surname": "G"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)