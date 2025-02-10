from app.core.database import users_collection
from bson import ObjectId
from typing import Optional

class UserRepository:
    """ 사용자 저장소 (MongoDB와 상호작용) """

    @staticmethod
    async def create(user: dict) -> str:
        """MongoDB에 사용자 생성"""
        result = await users_collection.insert_one(user)
        return str(result.inserted_id) 

    @staticmethod
    async def get_by_email(email: str) -> Optional[dict]:
        """이메일로 사용자 조회"""
        user = await users_collection.find_one({"email": email})
        if user:
            user["id"] = str(user["_id"]) 
            del user["_id"]  
        return user

    @staticmethod
    async def get_by_id(user_id: str) -> Optional[dict]:
        """ID로 사용자 조회"""
        if not ObjectId.is_valid(user_id):
            return None

        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"]) 
            del user["_id"] 
        return user
