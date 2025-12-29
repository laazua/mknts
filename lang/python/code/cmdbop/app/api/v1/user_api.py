"""
用户相关接口
"""
from fastapi import APIRouter

from app.service.user_service import UserServiceDep
from app.model.user_schema import UserCreate, UserUpdate, ResponseUser


user_router: APIRouter = APIRouter(tags=["用户管理"])


@user_router.post(
    "/user",
    response_model=ResponseUser,
)
async def create(user: UserCreate, service: UserServiceDep):
    """新增用户接口"""
    return await service.add_user(user)


@user_router.delete("/user/{id}")
async def delete(id: int, service: UserServiceDep): # pylint: disable=redefined-builtin
    """删除用户接口"""
    return await service.delete_user(id)


@user_router.put("/user/{id}")
async def update(id: int, user: UserUpdate, service: UserServiceDep): # pylint: disable=redefined-builtin
    """更新用户接口"""
    return await service.update_user(id, user)


@user_router.get("/user")
async def get_users(service: UserServiceDep):
    """用户列表接口"""
    return await service.get_users()


@user_router.get("/user/{id}")
async def retrieve(id: int, service: UserServiceDep): # pylint: disable=redefined-builtin
    """用户查询接口"""
    return await service.get_user_by_id(id)
