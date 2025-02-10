from app.core.database import comments_collection
from app.domain.entities.comment import Comment
from bson import ObjectId

class CommentRepository:
    """ 댓글 데이터베이스 접근 계층 """

    @staticmethod
    async def create(comment: Comment):
        """ 댓글 생성 """
        comment_dict = comment.dict()
        result = await comments_collection.insert_one(comment_dict)
        return str(result.inserted_id)

    @staticmethod
    async def get_by_post_id(post_id: str):
        """ 특정 게시글의 모든 댓글 조회 """
        if not ObjectId.is_valid(post_id):
            return None
        comments = []
        async for comment in comments_collection.find({"post_id": post_id}):
            comment["id"] = str(comment["_id"])
            del comment["_id"]
            comments.append(comment)
        return comments
