# @Time:        2022-08-04
# @Author:      Sseve
# @File:        __init__.py
# @Description: some utils
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from .middleware import AllowIps
from .remoteCmd import hand_zone, hand_host
from .password import hashed_pwd, verify_pwd
from .token import create_token, verify_token
from .response import Response


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/api/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)
            

__all__ = [AllowIps, hashed_pwd, verify_pwd, create_token, Response, get_current_user, hand_zone, hand_host]
