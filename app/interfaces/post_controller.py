from fastapi import APIRouter, HTTPException
from app.services.post_service import PostService
from app.domain.entities.post import Post

router = APIRouter(prefix="/posts", tags=["Posts"])  # ✅ "Posts" 그룹 추가

@router.post("/", summary="게시글 생성", description="새로운 게시글을 작성합니다.")
async def create_post(post: Post):
    post_id = await PostService.create_post(post)
    return {"id": post_id, **post.dict()}

@router.get("/{post_id}", summary="게시글 조회", description="MongoDB에서 특정 게시글을 조회합니다.")
async def get_post(post_id: str):
    post = await PostService.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
