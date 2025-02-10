from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    """ 게시글 엔티티 """
    title: str
    content: str
    author_id: str  # 작성자 ID (users 컬렉션 참조)
