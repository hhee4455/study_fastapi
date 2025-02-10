from pydantic import BaseModel

class Comment(BaseModel):
    """ 댓글 엔티티 """
    post_id: str  # 게시글 ID (posts 컬렉션 참조)
    author_id: str  # 작성자 ID (users 컬렉션 참조)
    content: str
