import os
from pymongo import MongoClient
import gridfs

DATABASE_URL = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = "ml_api_db"

client = MongoClient(DATABASE_URL)
db = client[DATABASE_NAME]
fs = gridfs.GridFS(db)

def get_db():
    return db
