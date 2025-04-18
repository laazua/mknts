# -*- coding: utf-8 -*-
"""
用户登录注册接口
通过角色分配不同的访问权限
"""

from app import router
from fastapi.requests import Request
from app.schemas.request import UserRegister
from app.db import query, insert, delete
from app.common import hash_password, white_list


@router.get("/login")
async def login(username: str, password: str, request: Request):
    ret = white_list(request)    # 可以以fastapi dependence的形式加在每个接口上
    if ret:
        return {"code": "-5", "message": "黑名单ip,不允许访问!"}

    if username and password:
        userdb = query(username)

    if userdb:
        if username == userdb.name and hash_password(password) == userdb.password:
            return {"code": "0", "message": "登录成功.", "role": userdb.role}
        else:
            return {"code": "-1", "message": "用户或密码不正确!"}
    else:
        return {"code": "-2", "message": "该用户不存在!"}


@router.post("/register")
async def register(userin: UserRegister):
    if userin:
        userdb = query(userin.name)
    if userdb:
        return {"code": "-3", "message": "用户名已经注册!"}
    else:
        # 往数据库中添加用户信息
        ret = insert(userin.name, userin.password, userin.role)
        if not ret:
            return {"code": "0", "message": "注册成功."}
        else:
            return {"code": "-4", "message": "注册失败!"}


@router.get("/delete")
async def delete_user(username: str):
    if username:
        if delete(username):
            return {"code": "0", "message": "删除用户成功"}
        else:
            return {"code": "-7", "message": "删除用户失败"}
