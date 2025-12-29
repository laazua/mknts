"""
用户数据模型定义
"""
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    """"用户基础模型"""
    username: str
    email: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """"用户创建模型"""
    password: str  # 创建时需要密码


class UserUpdate(BaseModel):
    """更新用户模型"""
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    full_name: Optional[str] = None


class UserInDB(UserBase):
    """数据库中的用户模型"""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ResponseUser(UserInDB):
    """响应用户模型"""
