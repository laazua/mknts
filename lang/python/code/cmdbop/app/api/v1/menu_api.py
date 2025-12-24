"""
菜单接口
"""

from fastapi import APIRouter


menu_router = APIRouter(tags=["菜单管理"])


@menu_router.post("/menu")
async def create():
    """新增菜单接口"""
    return {"message": "Create menu"}


@menu_router.delete("/menu/{id}")
async def delete(id: int):
    """删除菜单接口"""
    return {"message": f"Delete menu {id}"}


@menu_router.put("/menu/{id}")
async def update(id: int):
    """更新菜单接口"""
    return {"message": f"Update menu {id}"}


@menu_router.get("/menu")
async def list():
    """菜单列表接口"""
    return {"message": "List menus"}


@menu_router.get("/menu/{id}")
async def retrieve(id: int):
    """菜单查询接口"""
    return {"message": f"Retrieve menu {id}"}
