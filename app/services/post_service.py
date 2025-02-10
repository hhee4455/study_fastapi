from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class PostService:
    """ 게시글 비즈니스 로직 """

    @staticmethod
    async def create_post(post: Post):
        """ 게시글 생성 로직 """
        return await PostRepository.create(post)

    @staticmethod
    async def get_post(post_id: str):
        """ 게시글 조회 로직 """
        return await PostRepository.get_by_id(post_id)
