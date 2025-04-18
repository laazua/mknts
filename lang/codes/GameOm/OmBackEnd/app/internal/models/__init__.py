# @Time:        2022-08-04
# @Author:      Sseve
# @File:        __init__.py
# @Description: all api schemas

from pydantic import BaseModel
from typing import Dict, List, Any


class UserSign(BaseModel):
    """user login model"""
    name:     str
    password: str


class User(BaseModel):
    """add user model"""
    name:     str = None
    pwd_one:  str = None
    pwd_tow:  str = None
    desc:     str = None
    roles:    List[str] = None
    avatar:   str = None


# class TokenData(BaseModel):
#     username: str
#     roles:    List[str]


class ZoneAdd(BaseModel):
    """zone add model"""

    zones:    List[Dict[str, Any]]


class ZoneManage(BaseModel):
    """zone manage model"""
    target:   str
    zones:    List[Dict[str, Any]]


class Zone(BaseModel):
    target:   str
    zones:    List[Dict[str, Any]]