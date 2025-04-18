# -*- coding: utf-8 -*-
"""
配置文件的获取
"""

import os
import yaml

path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(path, 'config/app.yaml')


def get_config(section: str, filname=config_file):
    try:
        with open(filname, 'r') as fd:
            for key, value in (yaml.load(fd, Loader=yaml.FullLoader)).items():
                if key == section:
                    return value
    except yaml.YAMLError as error:
        print("Get config error: ", error)
