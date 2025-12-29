"""
登录和登出接口
"""
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.service.auth_service import AuthServiceDep
from app.model.auth_schema import AuthSchema, AuthResponse


auth_router = APIRouter(tags=["认证管理"])


@auth_router.post(
    "/login",
    response_model=AuthResponse,
    response_class=ORJSONResponse
)  # 使用更快的json响应: uv add orjson
async def login(
    auth_data: AuthSchema,
    service: AuthServiceDep,
):
    """用户登录接口"""
    return await service.sigin(auth_data)


@auth_router.post("/logout")
async def logout(service: AuthServiceDep):
    """用户登出接口"""
    return await service.logout()
