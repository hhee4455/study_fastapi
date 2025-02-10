from app.domain.repositories.post_repository import PostRepository
from app.domain.schemas.post_schema import PostCreateSchema, PostResponseSchema
from typing import Optional

class PostService:
    """ 게시글 비즈니스 로직 """

    @staticmethod
    async def create_post(post: PostCreateSchema) -> str:
        """ 게시글 생성 로직 """
        return await PostRepository.create(post)

    @staticmethod
    async def get_post(post_id: str) -> Optional[PostResponseSchema]:
        """ 게시글 조회 로직 """
        post = await PostRepository.get_by_id(post_id)
        return PostResponseSchema(**post) if post else None
