"""
认证仓库模块
"""
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select

from app.shared.db import DbSession
from app.model.auth_schema import AuthSchema
from app.model.user_model import User


class AuthRepository:
    """认证仓库类"""

    def __init__(self, session: DbSession):
        self.session = session

    async def auth(self):
        """认证"""

    async def get_user_info(self, auth_schema: AuthSchema) -> User:
        """获取用户信息"""
        stmt = select(User).where(User.username == auth_schema.username)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user

    def __call__(self, *args, **kwds):
        """实现可调用类,用于依赖注入"""
        return self


# def get_auth_repository(
#     session: DbSession = DbSession,
# ) -> AuthRepository:
#     """提供认证仓库实例"""
#     return AuthRepository(session=session)


# auth_repository 依赖注入
AuthRepositoryDep = Annotated[AuthRepository, Depends(AuthRepository)]
