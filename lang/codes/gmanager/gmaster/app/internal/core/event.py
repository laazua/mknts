from fastapi import FastAPI
from typing import Callable
from internal.core.mlog import logger
from internal.db.mongo import init_mongo, close_mongo
from internal.db.redis import sys_cache, code_cache


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        app.state.db = await init_mongo()
        logger.info("启动mongodb成功")
        app.state.sys_cache = await sys_cache()
        logger.info("启动redis成功")
        app.state.code_cache = await code_cache()

    return app_start


def shutdown(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_mongo()
        logger.info("关闭mongodb成功")
        await app.state.sys_cache.close()
        logger.info("关闭redis成功")
        await app.state.code_cache.close()

    return stop_app
    