"""
处理http请求:
  1.权限验证
  2.入参校验,封装,转发到service
  3.不包含业务逻辑,只做参数转换和结果封装
"""
from starlette.requests import Request
from starlette.endpoints import HTTPEndpoint

from .schemas import AuthDto
from .schemas import AuthSuccess
from .schemas import AuthFailure
from app.core.log import logger

class AuthController(HTTPEndpoint):
    """用户认证并生成token"""
    async def post(self, request: Request):
        try:
            data = await request.json()
            auth_data = AuthDto(**data)
        except ValueError as e:
            return AuthFailure(message=e)
        service = request.app.state.auth_service
        ok, token = await service.authenticate(auth_data)
        if not ok: return AuthFailure(message="认证失败")
        return AuthSuccess(message="认证成功",token=token)


class UserController(HTTPEndpoint):
    async def get(self, request: Request):
        pass

    async def post(self, request: Request):
        pass

    async def put(self, request: Request):
        pass

    async def delete(self, request: Request):
        pass