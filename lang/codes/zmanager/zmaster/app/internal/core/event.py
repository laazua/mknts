from fastapi import FastAPI
from typing import Callable
from app.internal import db
from .app_log import logger


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        app.state.db = await db.init_mongo()
        logger.info("启动mongodb成功")
        app.state.rdb = await db.init_redis()
        logger.info("启动redis成功")

    return app_start


def shutdown(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await db.close_mongo()
        logger.info("关闭mongodb成功")
        await app.state.rdb.close()
        logger.info("关闭redis成功")

    return stop_app
