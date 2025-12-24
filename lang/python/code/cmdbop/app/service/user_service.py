"""
用户服务模块
"""
from fastapi import Depends

from app.repository import user_repository as user_repo
from app.model.user_schema import UserCreate, UserUpdate


class UserService:
    """用户服务类"""

    def __init__(self, user_repo: user_repo.UserRepository = Depends(user_repo.UserRepository)):
        self.repository = user_repo

    def add_user(self, in_user: UserCreate) -> user_repo.UserRepository.model:
        """添加新用户"""
        return self.repository.create(in_user)


def get() -> UserService:
    return UserService(repository=user_repo.get())
