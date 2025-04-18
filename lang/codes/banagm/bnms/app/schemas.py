# -*- coding:utf-8 -*-
# 

from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class Zone(BaseModel):
    """区服列表数据"""
    zones: List[Dict[str, Any]]


class Table(BaseModel):
    tb: str


class Zones(Table):
    num: int
    size: int


class ZoneOpen(Table):
    """区服开服数据"""
    serverId:   str
    serverName: str
    serverIp:   str


class TokenData(BaseModel):
    """token数据"""
    username: str
    rolename: str


class User(BaseModel):
    name: str


class UserLogin(User):
    password: str


class UserDb(UserLogin):
    rolename: str
    # avatar: str = 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
    avatar: str = "test"
    introduction: str = 'test'


class Project(BaseModel):
    proName: str


class Response(BaseModel):
    code: int
    data: Optional[None]
    msg: str