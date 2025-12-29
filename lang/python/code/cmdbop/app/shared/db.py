"""
数据库连接
"""
import typing
from contextlib import asynccontextmanager
from typing import AsyncIterator, AsyncGenerator, Annotated
from fastapi import Depends, Request
from sqlalchemy import select, update as sa_update, delete as sa_delete
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from app import config


class Base(DeclarativeBase):
    """异步数据库模型基类"""


class SessionManager:
    """异步数据库连接管理类"""

    def __init__(
        self,
        database_url: str,
        *,
        echo: bool = False,
        pool_size: int = config.get().db.pool_size,
        max_overflow: int = 20,
    ):
        self.engine = create_async_engine(
            database_url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            future=True,
        )

        self._session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False,
        )

    async def create_all(self):
        """创建所有表"""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def get(self) -> AsyncGenerator[AsyncSession, None]:
        """提供异步数据库会话"""
        async with self._session_factory() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.commit()  # 将 commit 移到 finally 中

    async def close(self):
        """关闭数据库连接"""
        if self.engine:
            await self.engine.dispose()


# 类型变量定义
# pylint: disable=invalid-name
ModelType = typing.TypeVar("ModelType")
CreateSchemaType = typing.TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = typing.TypeVar("UpdateSchemaType", bound=BaseModel)
SchemaType = typing.TypeVar("SchemaType", bound=BaseModel)


class RepositoryCURD(
    typing.Generic[ModelType, CreateSchemaType, UpdateSchemaType, SchemaType]
):
    """基础仓库类,提供CRUD操作"""

    def __init__(self, session: AsyncSession, model: typing.Type[ModelType]):
        self.session = session
        self.model = model

    async def add(self, obj_in: CreateSchemaType) -> ModelType:
        """添加新对象"""
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_in_data)
        self.session.add(db_obj)
        await self.session.flush()
        await self.session.refresh(db_obj)
        return db_obj

    async def remove(self, id_: int) -> bool:
        """删除对象"""
        stmt = sa_delete(self.model).where(self.model.id == id_)
        result = await self.session.execute(stmt)
        await self.session.flush()
        return result.rowcount > 0

    async def put(self, id_: int, obj_in: UpdateSchemaType) -> ModelType:
        """更新对象"""
        update_data = obj_in.model_dump(exclude_unset=True)
        if not update_data:
            return await self.get(id_)
        
        stmt = (
            sa_update(self.model)
            .where(self.model.id == id_)
            .values(**update_data)
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        await self.session.flush()
        updated_obj = result.scalar_one_or_none()
        if updated_obj:
            await self.session.refresh(updated_obj)
        return updated_obj

    async def get(self, id_: int) -> ModelType | None:
        """获取单个对象"""
        stmt = select(self.model).where(self.model.id == id_)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self, skip: int = 0, limit: int = 100) -> list[ModelType]:
        """获取对象列表"""
        stmt = select(self.model).offset(skip).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()


async def get_db(request: Request) -> SessionManager:
    """从 FastAPI app.state 中获取 Database"""
    return request.app.state.db_session


async def get_session(
    db: SessionManager = Depends(get_db),
) -> AsyncIterator[AsyncSession]:
    """提供数据库会话"""
    async with db.get() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

DbSession = Annotated[AsyncSession, Depends(get_session)]
