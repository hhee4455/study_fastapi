from app.core.database import posts_collection
from bson import ObjectId
from typing import Optional

class PostRepository:
    """ 게시글 데이터베이스 접근 계층 """

    @staticmethod
    async def create(post: dict) -> str:
        """ 게시글 생성 """
        result = await posts_collection.insert_one(post)
        return str(result.inserted_id)  

    @staticmethod
    async def get_by_id(post_id: str) -> Optional[dict]:
        """ 게시글 조회 """
        if not ObjectId.is_valid(post_id):
            return None
        post = await posts_collection.find_one({"_id": ObjectId(post_id)})
        if post:
            post["id"] = str(post["_id"])  
            del post["_id"]
        return post
