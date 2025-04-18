# -*- coding: utf-8 -*-

from pydantic import BaseModel
from fastapi import Query


class User(BaseModel):
    name: str = Query(..., description="user name", max_length=128)


class UserOut(User):
    token: str = Query(..., description="token", max_length=256)
    role: str = Query(..., description="role", max_length=128)


class UserIn(User):
    password: str = Query(..., description="password", max_length=128)


class UserRegister(User):
    password: str = Query(..., description="password", max_length=128)
    role: str = Query(..., description="role", max_length=128)


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str
