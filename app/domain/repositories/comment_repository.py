from app.core.database import comments_collection
from bson import ObjectId
from typing import Optional, List

class CommentRepository:
    """ 댓글 데이터베이스 접근 계층 """

    @staticmethod
    async def create(comment: dict) -> str:
        """ 댓글 생성 """
        result = await comments_collection.insert_one(comment)
        return str(result.inserted_id)  

    @staticmethod
    async def get_by_post_id(post_id: str) -> Optional[List[dict]]:
        """ 특정 게시글의 모든 댓글 조회 """
        if not ObjectId.is_valid(post_id):
            return None
        comments = await comments_collection.find({"post_id": ObjectId(post_id)}).to_list(length=100)
        for comment in comments:
            comment["id"] = str(comment["_id"])  
            del comment["_id"]
        return comments
