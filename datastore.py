from pymongo import MongoClient

mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["linq_db"]
collection = db["linq_collection"]

print("plug fits")