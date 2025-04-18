# -*- coding: utf-8 -*-

import configparser, sys

def get_key(section: str, filed:str) -> str:
    """
    :param section:
    :param filed:
    :return:
    """
    conf = configparser.ConfigParser()
    try:
        conf.read("../config/pack_tool.txt")
        value = conf.get(section, filed)
        return value
    except configparser.Error as e:
        print("get pack_tool.txt error!", e)
        sys.exit(1)