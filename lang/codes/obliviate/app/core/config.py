import pathlib
from starlette.config import Config


if pathlib.Path("./.env").exists():
    _config = Config(".env")
else:
    raise FileNotFoundError("请在运行目录下配置.env文件")

# app配置
DEBUG: bool = _config("DEBUG", cast=bool, default=False)
RELOAD: bool = _config("RELOAD", cast=bool, default=True)
WORKERS: int = _config("WORKERS", cast=int, default=1)
APP_PORT: int = _config("APP_PORT", cast=int, default=8000)
APP_ADDR: str = _config("APP_ADDR", cast=str, default="127.0.0.1")
APP_NAME: str = _config("APP_NAME", cast=str, default="app.main:application")
APP_LOG_LEVEL: str = _config("APP_LOG_LEVEL", cast=str, default="info")
UVCORN_LOG_LEVEL: str = _config("UVCORN_LOG_LEVEL", cast=str, default="info")
UVICORN_LOG_ACCESS: bool = _config("UVICORN_LOG_ACCESS", cast=bool, default=False)
# 数据库配置
DB_URL: str = _config("DB_URL", cast=str, default="sqlite+aiosqlite:///./obliviate.db")
DB_POOL_SIZE: int = _config("DB_POOL_SIZE", cast=int, default=5)
DB_POOL_RECYCLE: int = _config("DB_POOL_RECYCLE", cast=int, default=3600)
DB_POOL_TIMEOUT: int = _config("DB_POOL_TIMEOUT", cast=int, default=30)
DB_MAX_OVERFLOW: int = _config("DB_MAX_OVERFLOW", cast=int, default=10)
