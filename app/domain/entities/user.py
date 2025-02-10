from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    """ 사용자 엔티티 """
    name: str
    email: EmailStr
    age: Optional[int] = None
