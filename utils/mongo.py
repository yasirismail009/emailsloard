from pymongo import MongoClient

from core import secrets

# Make a single connection per host and use it through the lifetime of the app instead of making a separate connection
# for each request
# https://pymongo.readthedocs.io/en/stable/faq.html#how-does-connection-pooling-work-in-pymongo

client= MongoClient(host=secrets.MONGO_URI, maxPoolSize=2, waitQueueTimeoutMS=30 * 1000)

def get_collection(db, col):
    database = client[db]
    collection = database[col]
    return collection


