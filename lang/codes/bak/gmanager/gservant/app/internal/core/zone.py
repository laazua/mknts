import time


def add_zone(zone):
    """开服处理"""
    time.sleep(5)
    return "开服处理"


def upt_conf(zone):
    """更新配置"""
    time.sleep(5)
    return "更新配置"


def upt_bin(zone):
    """更新后端文件"""
    return "更新后端文件"


def zone_opt(zone):
    """区服[start,stop,check]"""
    return "区服操作"