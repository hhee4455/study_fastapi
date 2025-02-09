from fastapi import FastAPI
from app.interfaces.user_controller import router as user_router

app = FastAPI()

# API 라우터 등록
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "FastAPI + MongoDB 클린 아키텍처"}
