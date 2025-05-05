"""
XxxDto 数据校验
XxxSuccess 成功响应
XxxFailure 失败响应
"""

from typing import Optional

from pydantic import BaseModel
from starlette.responses import JSONResponse


class AuthDto(BaseModel):
    email: str
    password: str


class UserDto(BaseModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool


class AuthSuccess(JSONResponse):
    def __init__(
        self, 
        code: int = 200, 
        message: Optional[str] = "success", 
        token: Optional[str] = None, 
        **kwargs
    ):
        content = { "code": code, "message": message, "token": token }
        content.update(kwargs)
        super().__init__(content=content)


class AuthFailure(JSONResponse):
    def __init__(
        self,
        code: int = 401,
        message: Optional[str] = "failure",
        **kwargs
    ):
        content = { "code": code, "message": message }
        content.update(kwargs)
        super().__init__(content=content)