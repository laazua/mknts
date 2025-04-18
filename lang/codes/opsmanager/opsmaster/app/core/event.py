import typing
from fastapi import FastAPI
from app import AppLogger, AppConfig
from aioredis import Redis, ConnectionPool
from mongoengine import connect, disconnect


async def init_mongo() -> typing.Any:
    return connect(
        AppConfig.get("db", "dbname"),
        host=AppConfig.get("db", "host"),
        port=AppConfig.getint("db", "port"),
        # username=AppConfig.get("db", "username"),
        # password=AppConfig.get("db", "password")
    )


async def close_mongo() -> typing.Any:
    return disconnect(
        alias=AppConfig.get("db", "dbname")
    )


async def init_redis():
    return Redis(
        connection_pool=ConnectionPool.from_url(
            "redis://{0}:{1}".format(
                 AppConfig.get('redis', 'host'),
                 AppConfig.get('redis', 'port')
            ),
            db=AppConfig.getint("redis", "dbname"),
            encoding="utf-8",
            decode_response=True
        )
    )


def startup(app: FastAPI) -> typing.Callable:
    async def app_start() -> None:
        app.state.mdb = await init_mongo()
        AppLogger.info("获取mongo数据库实例成功")
        app.state.rdb = await init_redis()
        AppLogger.info("获取redis数据库实例成功")

    return app_start


def shutdown(app: FastAPI) -> typing.Callable:
    async def app_stop() -> None:
        await close_mongo()
        AppLogger.info("关闭mongo数据库实例成功")
        await app.state.rdb.close()
        AppLogger.info("关闭redis数据库实例成功")

    return app_stop