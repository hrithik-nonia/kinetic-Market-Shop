# built in module imports
from motor.motor_asyncio import AsyncIOMotorClient


# custom module imports
from app.config.setting import setting


class MongoDb:
  client: AsyncIOMotorClient = None
  database: None


mongodb = MongoDb()


# data base connection start
async def connect_to_mongo():
  mongodb.client = AsyncIOMotorClient(setting.MONGO_URI)
  mongodb.database = mongodb.client[setting.DATABASE_NAME]

  print(f"✅ Connected to MongoDB: {setting.DATABASE_NAME}")


# close data base connection
async def close_mongodb_connection():
  if mongodb.client:
    mongodb.client.close()
    print("🔌 MongoDB connection closed")


# create a function which provide data case connection in entire project
def get_database():
  return mongodb.database
