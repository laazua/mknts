import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import user, zone
from internal.core.event import startup, shutdown
from internal.core.exception import HTTPException, http_error_handler, \
    http422_error_handler, UnicornException, unicorn_exception_handler, \
    RequestValidationError


# 加载环境变量
load_dotenv(find_dotenv(), override=True)

# 实例化Fastapi
application = FastAPI(
    title=settings.APP_NAME,
    debug=settings.APP_DEBUG,
    description=settings.APP_DESC
)

# 事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", shutdown(application))

# 异常错误处理
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 中间件
application.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],
    allow_headers=["*"],allow_credentials=True)

# 路由挂载
application.include_router(user.router)
application.include_router(zone.router)


if __name__ == "__main__":
    uvicorn.run(
        "gmaster:application",
        port=settings.APP_PORT,
        host=settings.APP_HOST,
        reload=settings.APP_RELOAD
    )