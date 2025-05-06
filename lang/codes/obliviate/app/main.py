import uvicorn
from starlette.routing import Route
from starlette.applications import Starlette


import app.core.config as setting
from app.mods.user.endpoints import AuthController
from app.mods.user.endpoints import UserController
from app.core.db import DBEnvent
from app.core.log import LOGGING_CONFIG
from app.mods.user.service import AuthService
from app.mods.user.repository import AuthRepository


routes=[
    Route("/api/sign", AuthController),
    Route("/api/user", UserController),
]
application = Starlette(
    debug=setting.DEBUG,
    routes=routes,
    on_startup=[DBEnvent.startup],
    on_shutdown=[DBEnvent.shutdown],   
)

# 绑定service到application.state
auth_repository = AuthRepository()
application.state.auth_service = AuthService(auth_repository)

def main():
    uvicorn.run(
        setting.APP_NAME, 
        host=setting.APP_ADDR, 
        port=setting.APP_PORT,
        reload=setting.RELOAD,
        workers=setting.WORKERS,
        log_config=LOGGING_CONFIG,
        access_log=setting.UVICORN_LOG_ACCESS,
        log_level=setting.UVCORN_LOG_LEVEL,
    )


if __name__ == "__main__":
    main()   
