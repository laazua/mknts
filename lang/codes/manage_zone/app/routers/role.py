# @Time:        2022-08-04
# @Author:      Sseve
# @File:        role.py
# @Description: all api of role

from fastapi import APIRouter, Depends
from internal.utils import get_current_user

router = APIRouter(prefix="/role/api", tags=["role api"])


@router.post("/role")
async def role(_ = Depends(get_current_user)):
    pass


@router.delete("/role")
async def role(_ = Depends(get_current_user)):
    pass


@router.put("/role")
async def role(_ = Depends(get_current_user)):
    pass


@router.get("/role")
async def role(_ = Depends(get_current_user)):
    pass


@router.get("/roles")
async def role_list(_ = Depends(get_current_user)):
    pass
