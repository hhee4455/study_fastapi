from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """공통 사용자 스키마"""
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0)

    model_config = {"from_attributes": True}

class UserCreateSchema(UserBase):
    """사용자 생성 요청 스키마"""
    password: str = Field(..., min_length=6, max_length=100)

class UserResponseSchema(UserBase):
    """사용자 응답 스키마"""
    id: Optional[str] = Field(None, alias="_id") 
    created_at: datetime = Field(default_factory=datetime.utcnow)
