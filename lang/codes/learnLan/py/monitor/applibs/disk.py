# -*- coding: utf-8 -*-
"""
监控磁盘
"""
import time
import logging
from psutil import disk_partitions, disk_usage
from config import AppConfig
from .sendmsg import send_msg


def run():
    logger = logging.getLogger('app')
    logger.info("start monitor disk...")
    while True:
        partition = disk_partitions()
        for i in range(len(partition)):
            percent = disk_usage(partition[i].mountpoint).percent
            free = disk_usage(partition[i].mountpoint).free / ((2<<9)**3)
            if percent > AppConfig.disk:
                smsg = "IP: %s, MountPoint: %s disk UsedPercent: %s, disk Free: %.1fG".format(
                    AppConfig.ip, partition[i].mountpoint, percent, free
                )
                logger.info(smsg)
                send_msg(smsg)
        time.sleep(180)
