from app.core.database import database
from app.domain.entities.user import User
from bson import ObjectId

class UserRepository:
    @staticmethod
    async def create(user: User):
        user_dict = user.dict()
        result = await database.users.insert_one(user_dict)
        return str(result.inserted_id)

    @staticmethod
    async def get_by_id(user_id: str):
        if not ObjectId.is_valid(user_id):
            return None
        user = await database.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            del user["_id"]
        return user

    @staticmethod
    async def get_by_email(email: str):
        return await database.users.find_one({"email": email})

    @staticmethod
    async def delete(user_id: str):
        if not ObjectId.is_valid(user_id):
            return False
        result = await database.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
