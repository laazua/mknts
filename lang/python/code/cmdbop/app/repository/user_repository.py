"""
用户数据库库操作
"""

from fastapi import Depends
import sqlalchemy as sa
import sqlalchemy.ext.asyncio as sasync

from app.shared import db
from app.model.user_model import User
from app.model.user_schema import UserCreate, UserUpdate


class UserRepository(db.AsyncCRUDBase[User, UserCreate, UserUpdate]):
    """用户数据库操作类"""
    
    model = User

    def __init__(self, db=Depends(db.get)):
        self.db = db  # type: ignore

    async def get_by_username(
        self,
        username: str
    ) -> User | None:
        """通过用户名获取用户"""
        result = await self.db.execute(
            sa.select(self.model).where(self.model.username == username)
        )
        return result.scalars().first()
    
    async def get_by_email(
        self,
        email: str
    ) -> User | None:
        """通过邮箱获取用户"""
        result = await self.db.execute(
            sa.select(self.model).where(self.model.email == email)
        )
        return result.scalars().first()


def get() -> UserRepository:
    return UserRepository()