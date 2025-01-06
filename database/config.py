from pymongo.mongo_client import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URL"))