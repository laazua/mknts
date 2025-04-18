import mongoengine
from app import cfg


async def init_mongo():
    return mongoengine.connect(
        cfg.get("mongo", "dbname"),
        host=cfg.get('mongo', 'host'),
        port=cfg.getint('mongo', 'port')
    )


async def close_mongo():
    return mongoengine.disconnect(
        alias=f"{cfg.get('mongo', 'dbname')}"
    )
