"""
角色接口
"""

from fastapi import APIRouter


role_router = APIRouter(tags=["角色管理"])


@role_router.post("/role")
async def create():
    """新增角色接口"""
    return {"message": "Create role"}


@role_router.delete("/role/{id}")
async def delete(id: int):
    """删除角色接口"""
    return {"message": f"Delete role {id}"}


@role_router.put("/role/{id}")
async def update(id: int):
    """更新角色接口"""
    return {"message": f"Update role {id}"}


@role_router.get("/role")
async def list():
    """角色列表接口"""
    return {"message": "List roles"}


@role_router.get("/role/{id}")
async def retrieve(id: int):
    """角色查询接口"""
    return {"message": f"Retrieve role {id}"}
