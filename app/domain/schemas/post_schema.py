from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    """게시글 공통 스키마"""
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10)
    author_id: str = Field(..., alias="author_id") 

    model_config = {"from_attributes": True}

class PostCreateSchema(PostBase):
    """게시글 생성 요청 스키마"""

class PostUpdateSchema(BaseModel):
    """게시글 수정 요청 스키마"""
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = Field(None, min_length=10)

class PostResponseSchema(PostBase):
    """게시글 응답 스키마"""
    id: Optional[str] = Field(None, alias="_id") 
    created_at: datetime = Field(default_factory=datetime.utcnow)
