import os
from configparser import ConfigParser


def _get_cfg() -> ConfigParser:
    cfg_file = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))) + "/app.ini"
    cfg = ConfigParser()
    cfg.read(cfg_file, "utf-8")

    return cfg


cfg = _get_cfg()
