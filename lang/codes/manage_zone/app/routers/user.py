# @Time:        2022-08-04
# @Author:      Sseve
# @File:        user.py
# @Description: all api of user

from fastapi import APIRouter, Depends
from internal.models import UserAdd
from fastapi.security import OAuth2PasswordRequestForm
from internal.utils import TokeHandle, get_current_user
from config import settings


router = APIRouter(prefix="/user/api", tags=["user api"])


@router.post("/login")
async def login(sign: OAuth2PasswordRequestForm = Depends()):
    """
    Args:
        @sign => {"name": "xxx", "password": "xxx"}
    Return:
    """
    # print(sign.username, sign.password)
    data = {"username":sign.username, "rolename":"admin"}
    token = TokeHandle(crt_key=settings.app_key, algorithm=settings.app_algorithm, 
                       expire_time=settings.app_expire_time, data=data).create_token
    print("token: ", token)


@router.post("/user")
async def user(add: UserAdd, _ = Depends(get_current_user)):
    """
    Args:
        @add => {"name": "xxx", "pwd_one": "xxx", "pwd_tow": "xxx"}
    Return:
    """
    print(add)


@router.delete("/user")
async def user(_ = Depends(get_current_user)):
    pass


@router.put("/user")
async def user(token_data: str = Depends(get_current_user)):
    print(token_data)


@router.get("/user")
async def user(_ = Depends(get_current_user)):
    pass


@router.get("/users")
async def user_list(_ = Depends(get_current_user)):
    pass
