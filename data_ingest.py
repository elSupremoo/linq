from pymongo import MongoClient
import random

mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["linq_db"]
collection = db["linq_collection"]

ranks = ["Silver", "Gold Nova", "Master Guardian", "Global Elite"]
pewpews= ["AWP", "AK-47", "M4A4", "Deagle"]

data = []

for i in range(100):
    data.append({
        "rank": random.choice(ranks),
        "fav_pewpew": random.choice(pewpews),
        "kdr": (random.randint(0, 100) / 10),
    })

collection.insert_many(data)
print("data ingested good")