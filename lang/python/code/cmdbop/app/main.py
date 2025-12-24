from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.shared import db
from app.config import con
from app.api.v1.auth_api import auth_router
from app.api.v1.user_api import user_router
from app.api.v1.role_api import role_router
from app.api.v1.menu_api import menu_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时初始化
    config = db.Config(
        database_url=f"mysql+aiomysql://{con.db.user}:{con.db.password}@{con.db.host}:{con.db.port}/{con.db.name}?charset=utf8mb4",
        pool_size=con.db.pool_size,
        echo=False,
        echo_pool=False
    )

    db_service = db.AsyncService()
    await db_service.init_app(config)
    app.state.db_service = db_service
    
    yield
    
    # 资源清理
    print("Shutting down application...")
    await db_service.close()


_app = FastAPI(
    debug=con.app_debug,
    title=con.app_title,
    description=con.app_description,
    version=con.app_version,
    lifespan=lifespan,
)
_app.include_router(auth_router, prefix=con.api.prefix)
_app.include_router(user_router, prefix=con.api.prefix)
_app.include_router(role_router, prefix=con.api.prefix)
_app.include_router(menu_router, prefix=con.api.prefix)


async def main():
    uvicorn.run(
        con.app_instance,
        host=con.api.host,
        port=con.api.port,
        reload=con.api.reload,
        workers=con.api.workers,
    )
