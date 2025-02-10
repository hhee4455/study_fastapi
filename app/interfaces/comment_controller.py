from fastapi import APIRouter, HTTPException
from app.services.comment_service import CommentService
from app.domain.entities.comment import Comment

router = APIRouter(prefix="/comments", tags=["Comments"])  # ✅ "Comments" 그룹 추가

@router.post("/", summary="댓글 생성", description="게시글에 댓글을 작성합니다.")
async def create_comment(comment: Comment):
    comment_id = await CommentService.create_comment(comment)
    return {"id": comment_id, **comment.dict()}

@router.get("/{post_id}", summary="댓글 조회", description="특정 게시글의 모든 댓글을 조회합니다.")
async def get_comments(post_id: str):
    comments = await CommentService.get_comments_by_post(post_id)
    if comments is None:
        raise HTTPException(status_code=404, detail="Post not found or no comments")
    return comments
