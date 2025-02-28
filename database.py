import config
import pymongo

class MongoDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient(config.MONGODB_URL)
        self.database = self.client[config.TASK_DATABASE_NAME]
        print("Connected to the MongoDB database!")

    def shutdown():
        self.client.close()
        print("MongoDB client closed!")