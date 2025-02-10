from fastapi import APIRouter, HTTPException
from app.services.comment_service import CommentService
from app.domain.schemas.comment_schema import CommentCreateSchema, CommentResponseSchema
from typing import List

router = APIRouter(prefix="/comments", tags=["Comments"]) 

@router.post("/", response_model=CommentResponseSchema, summary="댓글 생성", description="새로운 댓글을 작성합니다.")
async def create_comment(comment: CommentCreateSchema):
    """ 댓글 생성 엔드포인트 """
    comment_id = await CommentService.create_comment(comment)
    if comment_id is None:
        raise HTTPException(status_code=400, detail="Post not found")
    return CommentResponseSchema(id=comment_id, **comment.model_dump())

@router.get("/{post_id}", response_model=List[CommentResponseSchema], summary="댓글 조회", description="특정 게시글의 모든 댓글을 조회합니다.")
async def get_comments(post_id: str):
    """ 특정 게시글의 댓글 조회 엔드포인트 """
    comments = await CommentService.get_comments_by_post(post_id)
    if not comments:
        raise HTTPException(status_code=404, detail="Post not found or no comments")
    return comments
