"""
登录登出服务类
"""
from fastapi import Depends

from app.repository import auth_repository
from app.model.auth_schema import AuthSchema, AuthResponse

class AuthService:
    def __init__(self, auth_repo = Depends(auth_repository.get)):
        self.repository = auth_repo  # typing: ignore

    async def sigin(self, auth_schema: AuthSchema) -> AuthResponse:
        db_user = self.get_user_info(auth_schema)
        data = {'token': 'xndjafdf'}
        return AuthResponse(msg='登录成功', data=data)

    async def get_user_info(self, auth_schema: AuthSchema):
        pass


def get() -> AuthService:
    return AuthService()