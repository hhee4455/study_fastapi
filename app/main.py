from fastapi import FastAPI
from app.interfaces.user_controller import router as user_router
from app.interfaces.post_controller import router as post_router
from app.interfaces.comment_controller import router as comment_router

app = FastAPI(
    title="FastAPI + MongoDB API",
    description="FastAPI를 사용하여 Users, Posts, Comments 관리하는 API",
    version="1.0.0",
    openapi_tags=[
        {"name": "Users", "description": "사용자 관련 API"},
        {"name": "Posts", "description": "게시글 관련 API"},
        {"name": "Comments", "description": "댓글 관련 API"},
    ],
)

# API 라우터 등록
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "FastAPI + MongoDB API"}
