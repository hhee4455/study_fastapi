from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]
        self.users = self.db["users"]

    def get_database(self):
        return self.db

database = Database()
