# -*- coding: utf-8 -*-
# 实例化fastapi实例

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import user, game
from app.database import db


DESCRIBLE = """
    1. 这是运维管理系统的web服务.
    2. 主要处理前端传入的各种数据.
"""


def get_app() -> FastAPI:
    app = FastAPI(
        debug=True, 
        title="运维管理系统", 
        description=DESCRIBLE)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(user.router)
    app.include_router(game.router)

    @app.on_event('startup')
    async def startup():
        await db.connect()

    @app.on_event('shutdown')
    async def shutdown():
        await db.disconnect()

    return app
