import os
import configparser


def _get_config() -> configparser.ConfigParser:
    """读取配置文件"""
    filename = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))
    ) + "/opsmaster.conf"
    config_file = configparser.ConfigParser()
    config_file.read(filename, "utf-8")
    
    return config_file


AppConfig = _get_config()
