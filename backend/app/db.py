from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://online_mongo_host:27017")
    print("Connected to MongoDB")

async def close_mongo_connection():
    db.client.close()
    print("Closed MongoDB connection")
