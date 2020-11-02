from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.Sales_DB
try:
    db.command("serverStatus")
except Exception as e:
    print(e)
else:
    print("You are connected!")
client.close()
