# @Time:        2022-08-04
# @Author:      Sseve
# @File:        user.py
# @Description: all api of user

from fastapi import APIRouter, Depends
from internal.models import User
from fastapi.security import OAuth2PasswordRequestForm
from internal.utils import verify_pwd, create_token, \
     Response, get_current_user
from internal.db.log import log_db
from internal.db.user import user_db


router = APIRouter(prefix="/user/api", tags=["user api"])


@router.post("/login", description="api ok")
async def login(sign: OAuth2PasswordRequestForm = Depends()):
    db_user = user_db.check(user=sign)
    # check user and password
    if not verify_pwd(sign.password, db_user.password):
        return {"msg": "passwd error"}
    data = {"username": db_user.name, "roles": db_user.roles}
    # create token
    token = create_token(data)
    return Response(20000, token=token)


@router.post("/user", description="api ok")
async def user(user: User, token_data: str = Depends(get_current_user)):
    # 访问接口写入数据库
    if not log_db.add(name=token_data['username'], action=f"add user {user.name}"):
        return Response(40000, msg="add log failed")
    if user.pwd_one != user.pwd_tow:
        return
    if not user_db.add(user):
        return Response(40000, msg="add user failed")
    return Response(20000, msg="add user success")


@router.delete("/user", description="api ok")
async def user(user: User, token_data = Depends(get_current_user)):
    if not log_db.add(name=token_data['username'], action=f"delete user {user.name}"):
        return Response(40000, msg="delete log failed")
    if not user_db.delete(user):
        return {"code": 40000}
    return Response(20000, msg="del user success")


@router.get("/user", description="api ok")
async def user(token_data: str = Depends(get_current_user)):
    """get user info: role and menus"""
    db_user = user_db.check(name=token_data['username'])
    data = {
        "role": db_user.roles,
        "desc": db_user.desc,
        "name": db_user.name,
        "avatar": db_user.avatar
    }
    return Response(20000, data=data)


@router.get("/users", description="api ok")
async def user_list(_ = Depends(get_current_user)):
    user_list = user_db.get()
    if user_list:
        return Response(20000, data=user_list)
    return Response(20000, msg="do not get user list")


@router.post("/logout", description="api ok")
async def logout(token_data: str = Depends(get_current_user)):
    del token_data
    return Response(20000, msg="logout success")