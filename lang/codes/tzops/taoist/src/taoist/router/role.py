from fastapi import APIRouter, Depends

from taoist.core.deps import current_active_user


router = APIRouter(prefix="/role", tags=["角色操作"])


@router.post(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def addition():
    """
    角色增加
    """


@router.delete(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def delete():
    """
    角色清除
    """


@router.put(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def update():
    """
    角色更新
    """


@router.get(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def query():
    """
    角色查询
    """
