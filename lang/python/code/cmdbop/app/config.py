"""
配置解析模块
"""

# pylint: disable=missing-function-docstring
from enum import Enum
from pathlib import Path
from typing import List, Optional

import yaml
from pydantic import BaseModel, Field, field_validator


class LogLevel(str, Enum):
    """日志级别枚举"""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class DatabaseConfig(BaseModel):
    """数据库配置"""

    host: str = "localhost"
    port: int = 3306
    user: str = ""
    password: str = ""
    name: str = ""
    pool_size: int = Field(default=10, ge=1, le=100)

    @classmethod
    @field_validator("host")
    def validate_host(cls, v):
        if not v:
            raise ValueError("Database host must not be empty!")
        return v

    @classmethod
    @field_validator("port")
    def validate_port(cls, v):
        if not 1024 <= v <= 65535:
            raise ValueError("Port must be between 1024 and 65535")
        return v

    @classmethod
    @field_validator("user")
    def validate_user(cls, v):
        if not v:
            raise ValueError("Database user must not be empty!")
        return v

    @classmethod
    @field_validator("password")
    def validate_password(cls, v):
        if not v:
            raise ValueError("Database password must not be empty!")
        return v

    @classmethod
    @field_validator("name")
    def validate_name(cls, v):
        if not v:
            raise ValueError("Database name must not be empty!")
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

    host: str = "127.0.0.1"
    port: int = 8000
    workers: int = 4
    cors_origins: List[str] = ["http://localhost:3000"]
    prefix: str = "/api"
    reload: bool = False


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
    api: APIConfig

    @classmethod
    @field_validator("app_instance")
    def validate_app_instance(cls, v):
        if not v:
            raise ValueError("app_instance must not be empty!")
        return v

    class Config:
        """允许通过属性名访问(点语法)"""

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
        with open(self.config_path, "r", encoding="utf-8") as f:
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
    """获取全局配置对象"""
    return ConfigManager("config.yaml").load()


con: AppConfig = get()


# 使用示例
if __name__ == "__main__":
    YAML = """config.yaml 内容：
    app_name: "MyAwesomeApp"
    debug: true
    log_level: DEBUG
    
    database:
      host: "localhost"
      port: 5432
      username: "admin"
      password: "secret123"
      db_name: "mydb"
      pool_size: 20
    
    redis:
      host: "redis-host"
      port: 6379
      password: "redis-pass"
    
    api:
      port: 8080
      cors_origins:
        - "http://localhost:3000"
        - "https://myapp.com"
    """
    print(YAML)
