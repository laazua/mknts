# -*- coding: utf-8 -*-

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name = "运维管理"
    app_desc = "运维管理后端接口"
    host = "0.0.0.0"
    port = 8080
    secret_key = "ommstest"
    iplist = ['127.0.0.1', '192.168.30.123']


class DBSettings(BaseSettings):
    url = "mysql+pymysql://test:123456@127.0.0.1:3306/opms"


setting = Settings()
db_setting = DBSettings()

__all__ = [setting, db_setting]
