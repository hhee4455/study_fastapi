from fastapi import APIRouter, HTTPException
from app.services.post_service import PostService
from app.domain.schemas.post_schema import PostCreateSchema, PostResponseSchema

router = APIRouter(prefix="/posts", tags=["Posts"])  

@router.post("/", response_model=PostResponseSchema, summary="게시글 생성", description="새로운 게시글을 작성합니다.")
async def create_post(post: PostCreateSchema):
    """ 게시글 생성 엔드포인트 """
    post_id = await PostService.create_post(post)
    return PostResponseSchema(id=post_id, **post.model_dump())

@router.get("/{post_id}", response_model=PostResponseSchema, summary="게시글 조회", description="특정 게시글을 조회합니다.")
async def get_post(post_id: str):
    """ 게시글 조회 엔드포인트 """
    post = await PostService.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
