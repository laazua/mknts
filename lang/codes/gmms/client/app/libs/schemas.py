# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Dict, List, Tuple


class CurrentUser(BaseModel):
    username: str


class Response(BaseModel):
    message: str
    code: int


class LoginForm(BaseModel):
    """登录请求体"""
    username: str
    password: str


class RegistrationForm(BaseModel):
    """注册请求体"""
    username: str
    password: str
    password2: str


class DeleteUserForm(BaseModel):
    index: int
    username: str


class UserLogForm(BaseModel):
    username: str
    datetime: str


class CreateProForm(BaseModel):
    proname: str


class OpenZoneForm(BaseModel):
    ip: str
    serverid: int
    proname: str


class ZoneCmdForm(BaseModel):
    zones: List[dict]
    cmd: str


class DeleteUserResponse(Response):
    pass


class LoginResponse(Response):
    token: str


class RegesteResponse(Response):
    username: str


class ListDictResponse(Response):
    data: List[dict]


class OpenZoneResponse(Response):
    pass


class ListResponse(Response):
    data: list