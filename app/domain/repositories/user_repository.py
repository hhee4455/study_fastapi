from app.core.database import users_collection
from app.domain.entities.user import User
from bson import ObjectId

class UserRepository:
    """ 사용자 데이터베이스 접근 계층 """
    
    @staticmethod
    async def create(user: User):
        """ 사용자 생성 """
        user_dict = user.dict()
        result = await users_collection.insert_one(user_dict)
        return str(result.inserted_id)

    @staticmethod
    async def get_by_id(user_id: str):
        """ 사용자 조회 """
        if not ObjectId.is_valid(user_id):
            return None
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            del user["_id"]
        return user
