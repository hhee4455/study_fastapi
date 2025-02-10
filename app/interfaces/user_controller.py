from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.domain.entities.user import User

router = APIRouter(prefix="/users", tags=["Users"])  # ✅ "Users" 그룹 추가

@router.post("/", summary="사용자 생성", description="새 사용자를 MongoDB에 저장합니다.")
async def create_user(user: User):
    user_id = await UserService.create_user(user)
    if user_id is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"id": user_id, **user.dict()}

@router.get("/{user_id}", summary="사용자 조회", description="MongoDB에서 특정 사용자를 조회합니다.")
async def get_user(user_id: str):
    user = await UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
