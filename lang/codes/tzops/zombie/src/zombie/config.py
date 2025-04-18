import os
from functools import lru_cache

from dotenv import load_dotenv


class Settings:
    if not os.path.exists(".env"):
        raise Exception(".env not exists.")

    env = load_dotenv(".env")

    # env配置项
    app_port: int = int(os.getenv("app_port"))


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
