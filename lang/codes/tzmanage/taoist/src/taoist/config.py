"""
应用配置
"""
import os
from dotenv import load_dotenv


# 加载配置
if os.path.exists(".env"):
    load_dotenv(".env")
else:
    raise FileNotFoundError(".env Not Found! please config it in current path.")


class Setting:
    """.env配置""" 
    DEBUG = os.getenv("DEBUG")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")
    WORKERS = os.getenv("WORKERS")
    TIMEOUT = os.getenv("TIMEOUT")
    PIDFILE = os.getenv("PIDFILE")
    LOGPATH = os.getenv("LOGPATH")
    LOGFORMAT = os.getenv("LOGFORMAT")
    LOGLEVEL  = os.getenv("LOGLEVEL")

    # DB配置
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")

    # REDIS配置
    RDS_HOST = os.getenv("RDS_HOST")
    RDS_PORT = os.getenv("RDS_PORT")
    RDS_USER = os.getenv("RDS_USER")
    RDS_PASS = os.getenv("RDS_PASS")


class DevSetting(Setting):
    """开发配置"""
    DEBUG = True
    PORT = 8883
    SECRET_KEY = "dev1234"


class TestSetting(Setting):
    """测试配置"""
    DEBUG = True
    PORT  = 8884
    SECRET_KEY = "test1234"


class ProdSetting(Setting):
    """生产配置"""
    DEBUG = False
    PORT  = 8885 
    SECRET_KEY = "prod1234"
    WORKERS = 8
    TIMEOUT = 120
