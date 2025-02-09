from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.domain.entities.user import User

router = APIRouter()

@router.post("/users/")
async def create_user(user: User):
    user_id = await UserService.create_user(user)
    if user_id is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"id": user_id, **user.dict()}

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    success = await UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
