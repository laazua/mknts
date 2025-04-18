"""
app配置
"""
from pydantic import BaseConfig


class AppConfig(BaseConfig):
    """app配置"""
    APP_NAME: str = "gmanager"
    APP_DESC: str = "区服管理工具"
    APP_DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8888
    APP_RELOAD: bool = True

    # token过期时间(小时)
    TOKEN_TIME: int = 24 
    TOKEN_KEY: str = "xxx"


settings = AppConfig()    
