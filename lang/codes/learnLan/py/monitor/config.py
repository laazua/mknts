# -*- coding: utf-8 -*-
"""
程序的配置文件
"""
import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    """
    app程序的一些配置
    """
    app_path = os.path.abspath(os.path.dirname(__file__))
    pid_file = os.path.join(app_path, 'app.pid')
    ding_url = ""
    ip = '127.0.0.1'
    inet = "ens33"

    disk = 80
    load = 50
    mem = 60
    net_in = 50
    net_out = 50

    user = "java"
