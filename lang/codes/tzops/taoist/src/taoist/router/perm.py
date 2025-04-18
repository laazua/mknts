from fastapi import APIRouter, Depends

from taoist.core.deps import current_active_user


router = APIRouter(prefix="/perm", tags=["权限操作"])


@router.post(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def addition():
    """
    权限增加
    """


@router.delete(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def delete():
    """
    权限清除
    """


@router.put(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def update():
    """
    权限更新
    """


@router.get(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def query():
    """
    权限查询
    """
