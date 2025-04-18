# -*- coding:utf-8 -*-
"""
该模块定义一些请求体模型,用于客户端发送数据到后端
"""
from typing import List, Optional

from pydantic import BaseModel, EmailStr
from fastapi import Query    # Query用于校验客户端发送的数据(查询参数)
from fastapi import Path     # Path用于校验客户端发送的数据(路径参数)\
from pydantic import Field   # Field用于请求模型内部声明校验


class Person(BaseModel):
    """
    demo
    """
    name: Optional[str] = None   # 可选字段,默认值None
    telephone: int = Query(...)    # 必须字段
    addr: Optional[str] = None
    age: int = Path(...)
    weight: float = Field(..., description="person is weight")


class Student(BaseModel):
    """
    demo
    """
    grade: int
    p: Optional[Person]    # 请求体模型嵌套

    # 给请求模型定义额外的信息,不会添加任何验证,仅仅用于文档
    class Config:
        schema_extra = {
            "Student": {
                "grade": 100,
                "person": {
                    "name": "zhangsan",
                    "telephone": 13888888888,
                    "addr": None,
                    "age": 12,
                    "weight": 99.9
                }
            }
        }


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(BaseModel):
    pass


class UserDB(UserBase):
    hashed_password: str

