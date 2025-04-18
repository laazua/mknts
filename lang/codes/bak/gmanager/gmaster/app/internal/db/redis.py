import os
from aioredis import Redis, ConnectionPool


##################### redis 操作 #####################
async def sys_cache() -> Redis:
    return Redis(connection_pool=ConnectionPool.from_url(
        f"redis://{os.getenv('rds_host', '127.0.0.1')}:{os.getenv('rds_port', 6379)}",
        db=os.getenv('rds_dbname', 0),
        encoding='utf-8',
        decode_response=True
    ))


async def code_cache() -> Redis:
    return Redis(
       connection_pool=ConnectionPool.from_url(
        f"redis://{os.getenv('rds_host', '127.0.0.1')}:{os.getenv('rds_port', 6379)}",
        db=os.getenv('rds_dbname', 1),
        encoding='utf-8',
        decode_response=True
    ) 
    )