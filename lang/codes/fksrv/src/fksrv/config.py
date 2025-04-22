import os
from functools import lru_cache
from dotenv import load_dotenv


class Settings:
    if not os.path.exists(".env"):
        raise Exception(".env not exists.")

    load_dotenv(".env")

    # env配置项
    app_name: int = os.getenv("app_name")
    app_host: str = os.getenv("app_host")
    app_port: int = os.getenv("app_port")
    app_debug: bool = os.getenv("app_debug")
    app_reload: bool = os.getenv("app_reload")
    app_workers: int = os.getenv("app_workers")
    app_timeout: int = os.getenv("app_timeout")
    app_loglevel: str = os.getenv("app_loglevel")
    app_accesslog: str = os.getenv("app_accesslog")
    app_pidfile: str = os.getenv("app_pidfile")
    app_daemon: bool = os.getenv("app_daemon")
    app_keyfile: str = os.getenv("app_keyfile")
    app_certfile: str = os.getenv("app_certfile")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
