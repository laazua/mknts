"""
认证服务类
"""
from typing import Annotated

from fastapi import Depends

from app.repository.auth_repository import AuthRepositoryDep
from app.model.auth_schema import AuthSchema, AuthResponse


class AuthService:
    """认证服务类"""

    def __init__(self, repository: AuthRepositoryDep):
        self.repository = repository

    async def sigin(self, auth_schema: AuthSchema) -> AuthResponse:
        """登录"""
        db_user = await self.get_user_info(auth_schema)
        if not db_user:
            return AuthResponse(msg="用户不存在", data=None)
        # 这里省略密码验证等逻辑
        # 生成token等逻辑
        data = {"token": "xndjafdf"}
        return AuthResponse(msg="登录成功", data=data)

    async def get_user_info(self, auth_schema: AuthSchema):
        """获取用户信息"""
        user = await self.repository.get_user_info(auth_schema)
        return user

    async def logout(self):
        """登出"""
        # 这里省略登出逻辑，如token作废等
        return {"message": "User logged out"}

    def __call__(self, *args, **kwds):
        return self


# def get_auth_service(
#         repository: AuthRepositoryDep,
# ) -> AuthService:
#     """提供认证服务实例"""
#     return AuthService(repository=repository)


# auth_service 依赖注入
AuthServiceDep = Annotated[AuthService, Depends(AuthService)]
