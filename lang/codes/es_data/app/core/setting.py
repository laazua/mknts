import os
import configparser


def _get_config():
    """读取配置文件"""
    filename = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))
    ) + "/../app.cfg"
    config_file = configparser.ConfigParser()
    config_file.read(filename, "utf-8")
    
    return config_file


config = _get_config()