# -*- coding: utf-8 -*-
"""
监控负载
"""

import time, logging
from psutil import cpu_count
from .sendmsg import send_msg
from config import AppConfig


def count_cpucores():
    """
    获取cpu cores
    :param: None
    :return: None
    """
    cpu_cores = 0
    with open("/proc/cpuinfo", "rb") as fd:
        lines = fd.readlines()

    for line in lines:
        if line.lower().startswith("cpu cores".encode()):
            cpu_cores = int(line.split(":".encode())[1].strip())
            break

    return cpu_cores


def get_cpuload() -> dict:
    """
    获取系统cpu load
    :param: None
    :return: None
    """
    cpu_load = {}
    with open("/proc/loadavg") as fd:
        lines = fd.read()

    cpu_load['1'] = lines.split()[0]
    cpu_load['5'] = lines.split()[1]
    cpu_load['15'] = lines.split()[2]

    return cpu_load


def run():
    logger = logging.getLogger('app')
    logger.info("start monitor load...")

    sigle_cpu_cores = count_cpucores()
    physical_cpu_cores = cpu_count(logical=False)

    if sigle_cpu_cores and physical_cpu_cores:
        cpu_cores = sigle_cpu_cores * physical_cpu_cores
    else:
        cpu_cores = cpu_count()

    load = AppConfig.load * float(cpu_cores)
    while True:
        cpu_loads = get_cpuload()
        if float(cpu_loads['15']) > load:
            smsg = "IP: %s, cpu cores: %s, cpu load: %s, %s, %s && please hand it." % (
                AppConfig.ip, cpu_cores, cpu_loads['1'], cpu_loads['5'], cpu_loads['15']
            )
            logger.info(smsg)
            send_msg(smsg)
        time.sleep(180)
