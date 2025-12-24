"""
接口模型定义
"""
import typing
from pydantic import BaseModel
from pydantic import ConfigDict


class UserCreate(BaseModel):
    """创建用户的接口模型"""
    username: str
    email: str
    password: str
    full_name: typing.Optional[str] = None
    password: str

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    """更新用户的接口模型"""
    email: typing.Optional[str] = None
    full_name: typing.Optional[str] = None
    is_active: typing.Optional[bool] = None
    password: typing.Optional[str] = None

    model_config = ConfigDict(from_attributes=True)