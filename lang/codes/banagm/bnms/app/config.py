# -*- coding: utf-8 -*-
# app配置
import os
from dataclasses import dataclass


@dataclass
class Config:
    """app配置类"""
    app_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    host: str = '0.0.0.0'
    port: int = 8888
    expire_minutes: int = 60
    key_word: str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    algorithms: str = 'HS256'
    
    ## 数据库配置信息
    db_url: str = 'mysql+pymysql://test:test123@101.132.245.153:3306/bnms'
    
    ## gmd程序配置
    mg_port = 2004
    game_dir = '/data/game/'
    game_alias = 'syf'
    bin_path = app_path + '/backsource'
    bin_script = 'remotecp.sh'

cnf = Config()
__all__ = [cnf]