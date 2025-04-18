import os
import configparser


def _get_cfg() -> configparser.ConfigParser:
    """获取配置文件对象"""
    cfg_file = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))) + "/zmaster.conf"
    app_cfg = configparser.ConfigParser()
    app_cfg.read(cfg_file, "utf-8")

    return app_cfg


cfg = _get_cfg()
