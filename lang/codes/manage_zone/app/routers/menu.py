# @Time:        2022-08-04
# @Author:      Sseve
# @File:        menu.py
# @Description: all api of menu

from fastapi import APIRouter, Depends
from internal.utils import get_current_user


router = APIRouter(prefix="/menu/api", tags=["menu api"])


@router.post("/menu")
async def menu(_ = Depends(get_current_user)):
    pass


@router.delete("/menu")
async def menu(_ = Depends(get_current_user)):
    pass


@router.put("/menu")
async def menu(_ = Depends(get_current_user)):
    pass


@router.get("/menu")
async def menu(_ = Depends(get_current_user)):
    pass


@router.get("/menus")
async def menu_list(_ = Depends(get_current_user)):
    pass
