from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# MongoDB 연결
client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]

# 여러 컬렉션 관리
users_collection = database["users"]
posts_collection = database["posts"]
comments_collection = database["comments"]
