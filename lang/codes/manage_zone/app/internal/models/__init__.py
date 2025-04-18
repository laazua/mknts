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


class UserAdd(BaseModel):
    """add user model"""
    name:     str
    pwd_one:  str
    pwd_tow:  str


class UserDel(BaseModel):
    """del user model"""
    name:     str


class TokenData(BaseModel):
    username: str
    rolename: str


class ZoneAdd(BaseModel):
    """zone add model"""
    zones:    List[Dict[str, Any]]


class ZoneManage(BaseModel):
    """zone manage model"""
    target:   str
    zones:    List[Dict[str, Any]]
