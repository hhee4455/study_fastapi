from app.domain.repositories.user_repository import UserRepository
from app.domain.schemas.user_schema import UserCreateSchema, UserResponseSchema
from typing import Optional

class UserService:
    """ 사용자 비즈니스 로직을 처리하는 서비스 계층 """

    @staticmethod
    async def create_user(user: UserCreateSchema) -> Optional[str]:
        """ 사용자 생성 로직 """
        existing_user = await UserRepository.get_by_email(user.email)
        if existing_user:
            return None  # 이메일 중복 방지

        user_dict = user.model_dump(exclude={"password"})  # 비밀번호 제외
        return await UserRepository.create(user_dict)

    @staticmethod
    async def get_user(user_id: str) -> Optional[UserResponseSchema]:
        """ 사용자 조회 로직 """
        user = await UserRepository.get_by_id(user_id)
        if user:
            return UserResponseSchema(**user)  # `_id` → `id` 변환 완료된 상태로 반환
        return None
