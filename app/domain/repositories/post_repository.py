from app.core.database import posts_collection
from app.domain.entities.post import Post
from bson import ObjectId

class PostRepository:
    """ 게시글 데이터베이스 접근 계층 """

    @staticmethod
    async def create(post: Post):
        """ 게시글 생성 """
        post_dict = post.dict()
        result = await posts_collection.insert_one(post_dict)
        return str(result.inserted_id)

    @staticmethod
    async def get_by_id(post_id: str):
        """ 게시글 조회 """
        if not ObjectId.is_valid(post_id):
            return None
        post = await posts_collection.find_one({"_id": ObjectId(post_id)})
        if post:
            post["id"] = str(post["_id"])
            del post["_id"]
        return post
