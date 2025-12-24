"""
用户相关接口
"""
from fastapi import APIRouter, Depends

from app.service import user_service
from app.model.user_schema import UserCreate


user_router = APIRouter(tags=["用户管理"])


@user_router.post("/user")
async def create(user: UserCreate, service=Depends(user_service.get)):
    """新增用户接口"""
    return service.add_user(user)


@user_router.delete("/user/{id}")
async def delete(id: int):
    """删除用户接口"""
    return {"message": f"Delete user {id}"}


@user_router.put("/user/{id}")
async def update(id: int):
    """删除用户接口"""
    return {"message": f"Update user {id}"}


@user_router.get("/user")
async def list():
    """用户列表接口"""
    return {"message": "List users"}


@user_router.get("/user/{id}")
async def retrieve(id: int):
    """用户查询接口"""
    return {"message": f"Retrieve user {id}"}
