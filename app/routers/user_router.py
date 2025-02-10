from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.domain.schemas.user_schema import UserCreateSchema, UserResponseSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseSchema, summary="사용자 생성", description="새 사용자를 MongoDB에 저장합니다.")
async def create_user(user: UserCreateSchema):
    """ 사용자 생성 엔드포인트 """
    user_id = await UserService.create_user(user)
    if user_id is None:
        raise HTTPException(status_code=400, detail="이메일이 이미 존재합니다")
    
    return UserResponseSchema(id=user_id, **user.model_dump(exclude={"password"}))

@router.get("/{user_id}", response_model=UserResponseSchema, summary="사용자 조회", description="MongoDB에서 특정 사용자를 조회합니다.")
async def get_user(user_id: str):
    """ 사용자 조회 엔드포인트 """
    user = await UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을수  없습니다.")
    return user
