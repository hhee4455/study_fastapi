from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class UserService:
    """ 사용자 비즈니스 로직을 처리하는 서비스 계층 """
    
    @staticmethod
    async def create_user(user: User):
        """ 사용자 생성 로직 """
        existing_user = await UserRepository.get_by_id(user.email)
        if existing_user:
            return None  # 이메일 중복 방지
        return await UserRepository.create(user)

    @staticmethod
    async def get_user(user_id: str):
        """ 사용자 조회 로직 """
        return await UserRepository.get_by_id(user_id)
