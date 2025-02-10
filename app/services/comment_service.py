from app.domain.repositories.comment_repository import CommentRepository
from app.domain.schemas.comment_schema import CommentCreateSchema, CommentResponseSchema
from typing import List, Optional

class CommentService:
    """ 댓글 비즈니스 로직 """

    @staticmethod
    async def create_comment(comment: CommentCreateSchema) -> Optional[str]:
        """ 댓글 생성 로직 """
        return await CommentRepository.create(comment)

    @staticmethod
    async def get_comments_by_post(post_id: str) -> List[CommentResponseSchema]:
        """ 특정 게시글의 댓글 조회 로직 """
        comments = await CommentRepository.get_by_post_id(post_id)
        return [CommentResponseSchema(**comment) for comment in comments] if comments else []
