"""
用户仓库模块
"""
from typing import Annotated
from fastapi import Depends
from app.model.user_model import User
from app.model.user_schema import UserCreate, UserUpdate
from app.shared.db import DbSession, RepositoryCURD


class UserRepository(RepositoryCURD[User, UserCreate, UserUpdate, User]):
    """用户数据库操作类"""
    model = User

    def __init__(self, session: DbSession):
        super().__init__(session, User)
        self.session = session

    async def create(self, user_create: UserCreate) -> User:
        """创建用户"""
        return await super().add(user_create)

    async def delete(self, id_):
        """删除用户"""
        return await super().remove(id_)

    async def update(self, id_, user_update: UserUpdate) -> User:
        """更新用户"""
        return await super().put(id_, user_update)

    async def get_by_id(self, id_) -> User:
        """通过ID获取用户"""
        return await super().get(id_)

    async def get_users(self, skip = 0, limit = 100):
        """获取用户列表"""
        return await super().list(skip, limit)

    def __call__(self, *args, **kwds):
        """实现可调用类,用于依赖注入"""
        return self


# def get_user_repository(
#     session: DbSession = DbSession,
# ) -> UserRepository:
#     """提供用户仓库实例"""
#     return UserRepository(session=session)


# user_repository 依赖注入
UserRepositoryDep = Annotated[UserRepository, Depends(UserRepository)]
