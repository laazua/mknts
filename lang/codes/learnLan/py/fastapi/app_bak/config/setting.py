# -*- coding: utf-8 -*-
import os
import yaml
from dataclasses import dataclass
from pydantic import BaseSettings


path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(path, 'app.yaml')


def get_config(section: str, filename=config_file):
    """通过yaml文件获取配置"""
    try:
        with open(filename, 'r') as fd:
            for key, value in (yaml.load(fd, Loader=yaml.FullLoader)).items():
                if key == section:
                    return value
    except yaml.YAMLError as error:
        print("Get config error: ", error)


class Base(BaseSettings):
    """该类中的数据通过实例对象调用"""
    app_name: str = "msop api"
    ip_list: list = ['127.0.0.1', '192.168.30.123']


class AppListenAddr(BaseSettings):
    """该类中的数据通过实例对象调用"""
    host: str = "0.0.0.0"
    port: int = 8080


class DataBase(BaseSettings):
    url: str = "mysql+pymysql://test:123456@127.0.0.1:3306/opms"


@dataclass
class DBConfig:
    """该类中的数据可以通过类名直接调用"""
    url: str = "mysql+pymysql://test:123456@127.0.0.1:3306/opms"


base = Base()
app_address = AppListenAddr()
data_base = DataBase()