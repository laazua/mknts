"""
项目配置
"""

import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    这里的类变量需定义类型,
    与.env中的配置变量对应
    """

    if not os.path.exists(".env"):
        raise Exception(".env not exists!")

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    # 应用配置
    app_name: str = "^.^"
    app_debug: bool = True
    app_works: int = 1
    app_loglevel: str = "info"
    app_host: str = "localhost"
    app_port: int = 7000
    app_reload: bool = False
    app_version: str = "0.0.1"
    app_summary: str
    app_description: str
    app_prefix: str | None = None
    app_secret: str | None = None
    app_algorithm: str | None = None
    app_expire_time: int = 3600

    # mysql数据库配置
    db_user: str | None = None
    db_pass: str | None = None
    db_port: int = 3306
    db_host: str | None = None
    db_name: str | None = None

    # class Config:
    #     env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
