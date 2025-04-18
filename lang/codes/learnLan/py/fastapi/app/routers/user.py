# -*- coding: utf-8 -*-

from fastapi import (
    APIRouter, Form, Depends)

from app.db.database import (
    query, query_user, add_user, delete_user, change_password)
from app.common.jwt import Token
from app.dependencies.utils import allow_ip

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...), is_allow: bool = Depends(allow_ip)):
    """
    验证用户是否存在,并生成token
    :param username:
    :param password:
    :param is_allow:
    :return:
    """
    if not is_allow:
        return {
           "message": "client ip not allow visit this server!"
        }
    # query database
    user = query_user(username, Token.hash_password(password))
    if not user:
        return {
            "message": "username or password error!"
        }
    else:
        return {
            "message": "login successful.",
            "token": Token.encode(**user)
        }


@router.post("/register")
async def register(username: str = Form(...), password: str = Form(...), rolename: str = Form(...)):
    if not query_user(username, Token.hash_password(password)):
        add_user(username, Token.hash_password(password), rolename)
    return {
        "message": "register successful."
    }


@router.post("/deleteUser")
async def del_user(username: str = Form(...)):
    if query(username):
        if delete_user(username):
            return {
                "message": "delete user successful."
            }
        else:
            return {
                "message": "delete user failed."
            }
    else:
        return {
            "message": "this user not in database."
        }


@router.post("/changePassword")
def change_pw(username: str = Form(...), password: str = Form(...), new_password: str = Form(...)):
    ret = change_password(username, Token.hash_password(password), Token.hash_password(new_password))
    if not ret:
        return {
           "message": "change password failed."
        }
    else:
        return {
            "message": "change password successful."
        }


@router.post("/userInfo")
async def user_info(token: str = Form(...)):
    """
    根据用户token信息获取用户的完整信息返回给前端分配相应的页面权限
    :return:
    """
    data = Token.decode(token)
    print(data)
