"""应用入口文件"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app import config
from app.shared import db
from app.shared import redis
from app.api.v1.auth_api import auth_router
from app.api.v1.user_api import user_router
from app.api.v1.role_api import role_router
from app.api.v1.menu_api import menu_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时初始化
    db_session = db.SessionManager(
        f"mysql+aiomysql://{config.get().db.user}:{config.get().db.password}@{config.get().db.host}:\
            {config.get().db.port}/{config.get().db.name}?charset=utf8mb4"
    )
    await db_session.create_all()
    redis_session = redis.Session()

    app.state.db_session = db_session
    app.state.redis_session = redis_session
    yield
    # 关闭时资源清理
    print("Shutting down application...")
    await db_session.close()
    await redis_session.close()


_app = FastAPI(
    debug=config.get().app_debug,
    title=config.get().app_title,
    description=config.get().app_description,
    version=config.get().app_version,
    lifespan=lifespan,
)
_app.include_router(auth_router, prefix=config.get().api.prefix)
_app.include_router(user_router, prefix=config.get().api.prefix)
_app.include_router(role_router, prefix=config.get().api.prefix)
_app.include_router(menu_router, prefix=config.get().api.prefix)


async def main():
    """应用主函数"""
    uvicorn.run(
        config.get().app_instance,
        host=config.get().api.host,
        port=config.get().api.port,
        reload=config.get().api.reload,
        workers=config.get().api.workers,
    )
