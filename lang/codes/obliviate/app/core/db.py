from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

import app.core.config as setting
from app.core.log import logger

_engine = create_async_engine(
        setting.DB_URL, 
        echo=True, 
        pool_size=setting.DB_POOL_SIZE, 
        pool_recycle=setting.DB_POOL_RECYCLE,
        pool_timeout=setting.DB_POOL_TIMEOUT,
        max_overflow=setting.DB_MAX_OVERFLOW,
    )
# 创建异步db session
Session = sessionmaker(bind=_engine, class_=AsyncSession, expire_on_commit=False)


class DBEnvent:
    @staticmethod
    async def startup():
        logger.info("DB startup")
        async with _engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @staticmethod
    async def shutdown():
        logger.info("DB shutdown")
        await _engine.dispose()