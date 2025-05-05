from typing import Optional

from sqlmodel import select

from app.mods.user.models import User
from .schemas import AuthDto
from app.core.db import Session

class AuthRepository:
    async def authenticate(self, auth_data: AuthDto) -> Optional[bool]:
        async with Session() as session:
            statement = select(User).where(User.email == auth_data.email)
            user = await session.exec(statement)
            user = user.one_or_none()
            if not user: return False
        if not user: return False
        # 验证密码

        return True

class UserRepository:
    ...