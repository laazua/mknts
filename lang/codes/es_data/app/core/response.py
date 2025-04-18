"""封装app接口的返回格式"""
from typing import Any
from pydantic import BaseModel


class Failure(BaseModel):
    """失败状态数据返回格式"""
    code: int = None
    message: str = None


class Success(BaseModel):
    """成功状态数据返回格式"""
    code: int = 20000
    data: Any = None
    message: str = None