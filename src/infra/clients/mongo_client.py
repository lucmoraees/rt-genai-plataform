from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import os

class MongoClient:
  client: AsyncIOMotorClient = None
  db: AsyncIOMotorDatabase = None

  @classmethod
  def connect(cls):
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB")
    cls.client = AsyncIOMotorClient(mongo_uri)
    cls.db = cls.client[db_name]

  @classmethod
  def get_db(cls) -> AsyncIOMotorDatabase:
    if cls.db is None:
      raise RuntimeError("MongoDB not connected. Call MongoClient.connect() first.")
    return cls.db
  
  @classmethod
  async def create_indexes(cls):
    collection = cls.get_db()["history"]
    await collection.create_index("userId")
