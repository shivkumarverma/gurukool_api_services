from pymongo import MongoClient

client = MongoClient('mongodb://mongo:aU5YPTrXol5mWKcXLnhd@containers-us-west-98.railway.app:6363')
db = client.gurukool


def get_user(email):
    user = db.users.find_one({"email":email})
    return user