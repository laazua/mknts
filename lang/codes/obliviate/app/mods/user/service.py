"""
承载核心业务逻辑, 协调多种资源(如多个 DAO、第三方服务)的调用,并控制事务边界.
Service 层通常以接口加实现类方式存在,利于测试与替换
"""
from typing import Tuple, Optional

from .schemas import AuthDto
from .repository import AuthRepository


class AuthService:
    def __init__(self, repositry: AuthRepository):
        self.repositry = repositry
        
    async def authenticate(self, auth_data: AuthDto) -> Tuple[bool, Optional[str]]:
        ok =  await self.repositry.authenticate(auth_data)
        if not ok: return False, None
        # 生成token
        token = "token"
        return True, token