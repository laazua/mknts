# -*- coding: utf-8 -*-
"""
接口请求响应数据类型
"""

from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserDB(User):
    pass
