from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from typing import Optional
from datetime import datetime
from bson import ObjectId

class CommentBase(BaseModel):
    """댓글 공통 스키마"""
    content: str = Field(..., min_length=1, max_length=500)
    author_id: str = Field(..., alias="author_id") 
    post_id: str = Field(..., alias="post_id")  

    model_config = {"from_attributes": True}

class CommentCreateSchema(CommentBase):
    """댓글 생성 요청 스키마"""

class CommentUpdateSchema(BaseModel):
    """댓글 수정 요청 스키마"""
    content: Optional[str] = Field(None, min_length=1, max_length=500)

class CommentResponseSchema(CommentBase):
    """댓글 응답 스키마"""
    id: Optional[str] = Field(None, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
