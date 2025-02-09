from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class UserService:
    @staticmethod
    async def create_user(user: User):
        existing_user = await UserRepository.get_by_email(user.email)
        if existing_user:
            return None  # 이메일 중복 방지
        return await UserRepository.create(user)

    @staticmethod
    async def get_user(user_id: str):
        return await UserRepository.get_by_id(user_id)

    @staticmethod
    async def delete_user(user_id: str):
        return await UserRepository.delete(user_id)
