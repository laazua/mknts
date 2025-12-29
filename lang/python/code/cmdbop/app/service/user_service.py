"""
用户服务模块
"""
from typing import Annotated

from fastapi import Depends

from app.repository.user_repository import UserRepositoryDep
from app.model.user_schema import UserCreate, UserUpdate, ResponseUser


class UserService:
    """用户服务类"""
    def __init__(self, repository: UserRepositoryDep):
        self.repository= repository

    async def add_user(self, in_user: UserCreate) -> ResponseUser:
        """添加新用户"""
        return await self.repository.create(user_create=in_user)

    async def delete_user(self, id_: int):
        """删除用户"""
        return await self.repository.delete(id_)

    async def update_user(self, id_: int, in_user: UserUpdate) -> ResponseUser:
        """更新用户"""
        return await self.repository.update(id_, in_user)

    async def get_user_by_id(self, id_: int) -> ResponseUser:
        """通过ID获取用户"""
        return await self.repository.get_by_id(id_)

    async def get_users(self, skip: int = 0, limit: int = 100) -> list[ResponseUser]:
        """获取用户列表"""
        return await self.repository.get_users(skip, limit)

    def __call__(self, *args, **kwds):
        """实现可调用类,用于依赖注入"""
        return self


# # 创建依赖注入函数
# def get_user_service(
#     repository: UserRepositoryDep,
# ) -> UserService:
#     """获取用户服务实例"""
#     return UserService(repository=repository)


# 类型提示（用于 API 路由的依赖注入）
UserServiceDep = Annotated[UserService, Depends(UserService)]
