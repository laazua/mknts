# -*- coding: utf-8 -*-
"""
监控指定用户进程
"""
import time
import logging
from psutil import pids, Process
from config import AppConfig


def run():
    logger = logging.getLogger('app')
    logger.info("start monitor user...")
    while True:
        for pid in pids():
            p = Process(pid)
            if p.username() == AppConfig.user:
                cpu_time = p.cpu_times()
                mem = p.memory_info()
                print("cpu_time: ", cpu_time)
                print("mem: ", mem)
        time.sleep(180)
