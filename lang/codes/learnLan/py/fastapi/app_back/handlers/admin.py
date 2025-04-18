# -*- coding:utf-8 -*-
from fastapi import Body    # 请求体中的单一值校验

from app import router


@router.get('/admin', tags=['admin'])
async def admin(is_super: bool = Body(True, description="is admin")):
    """
    超级管理员，拥有app的所有权限
    :param is_super:
    :return:
    """
    return {"message": "admin", "super": is_super}
