import aioredis
from app import cfg


async def init_redis() -> aioredis.Redis:
    return aioredis.Redis(
        connection_pool=aioredis.ConnectionPool.from_url(
            f"redis://{cfg.get('redis', 'host')}:{cfg.get('redis', 'port')}",
            db=cfg.get('redis', 'dbname'),
            encoding="utf-8",
            decode_response=True
        )
    )
