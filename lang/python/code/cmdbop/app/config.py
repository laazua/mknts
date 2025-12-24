"""
配置解析模块
"""

# requirements.txt
# pydantic>=2.0
# pyyaml

import yaml
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from enum import Enum


# 定义配置模型
class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class DatabaseConfig(BaseModel):
    """数据库配置"""
    host: str = "localhost"
    port: int = 5432
    user: str
    password: str
    name: str
    pool_size: int = Field(default=10, ge=1, le=100)
    
    @field_validator('port')
    def validate_port(cls, v):
        if not 1024 <= v <= 65535:
            raise ValueError('Port must be between 1024 and 65535')
        return v


class RedisConfig(BaseModel):
    """Redis配置"""
    enabled: bool = True
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: Optional[str] = None


class APIConfig(BaseModel):
    """API配置"""
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    cors_origins: List[str] = ["http://localhost:3000"]
    prefix: str
    reload: bool = False

    @field_validator('prefix')
    def validate_prefix(cls, v):
        if not v:
            raise ValueError('api.prefix must not be empty!')
        return v


class AppConfig(BaseModel):
    """应用配置"""
    # 通过嵌套模型对应YAML中的对象
    app_title: str = "MyApp"
    app_description: str = Field()
    app_version: str = "v1.0"
    app_debug: bool = False
    log_level: LogLevel = LogLevel.INFO
    app_instance: str
    
    db: DatabaseConfig
    redis: RedisConfig
    api: APIConfig = Field(default_factory=APIConfig)
    
    @field_validator('app_instance')
    def validate_app_instance(cls, v):
        if not v:
            raise ValueError('app_instance must not be empty!')
        return v

    class Config:
        # 允许通过属性名访问（点语法）
        from_attributes = True


class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = Path(config_path)
        self._config: Optional[AppConfig] = None
    
    def load(self) -> AppConfig:
        """加载并解析配置"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        # 加载YAML
        with open(self.config_path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        
        # 转换为Pydantic模型
        self._config = AppConfig(**yaml_data)
        return self._config
    
    def get_config(self) -> AppConfig:
        """获取配置对象"""
        if self._config is None:
            self.load()
        return self._config
    
    # 使ConfigManager可像配置对象一样访问
    def __getattr__(self, name):
        return getattr(self.get_config(), name)


def get() -> AppConfig:
    manager = ConfigManager("config.yaml")
    config: AppConfig = manager.load()
    return config


manager = ConfigManager("config.yaml")
con: AppConfig = manager.load()

# 使用示例
if __name__ == "__main__":
    # config.yaml 内容：
    # app_name: "MyAwesomeApp"
    # debug: true
    # log_level: DEBUG
    # 
    # database:
    #   host: "localhost"
    #   port: 5432
    #   username: "admin"
    #   password: "secret123"
    #   db_name: "mydb"
    #   pool_size: 20
    # 
    # redis:
    #   host: "redis-host"
    #   port: 6379
    #   password: "redis-pass"
    # 
    # api:
    #   port: 8080
    #   cors_origins:
    #     - "http://localhost:3000"
    #     - "https://myapp.com"
    
    manager = ConfigManager("config.yaml")
    config: AppConfig = manager.load()
    
    # 使用点语法访问！
    print(config.app_name)          # MyAwesomeApp
    print(config.db.host)     # localhost
    print(config.db.port)     # 5432
    print(config.redis.host)        # redis-host
    print(config.api.cors_origins)  # ['http://localhost:3000', 'https://myapp.com']
    print(config.log_level.value)   # DEBUG