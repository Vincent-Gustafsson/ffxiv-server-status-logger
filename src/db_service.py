import os
from pymongo import MongoClient


cluster = MongoClient(os.environ.get("MONGODB_URL"))
db = cluster["ffxiv_scraper"]
collection = db["results"]


def add_log(ch, method, properties, body):
    log = collection.insert_one({
        "data": body.decode("utf-8")
    })
