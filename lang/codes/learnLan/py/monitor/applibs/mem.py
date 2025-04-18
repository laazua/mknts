# -*- coding: utf-8 -*-
"""
监控内存
"""

import time
import logging
from psutil import virtual_memory
from config import AppConfig
from .sendmsg import send_msg


def run():
    logger = logging.getLogger('app')
    logger.info("start monitor mem...")
    while True:
        percent = virtual_memory().percent
        available = virtual_memory().available / ((2<<9)**3)
        if percent > AppConfig.mem:
            smsg = "IP: %s, Mem Available: %.1fG, Mem UsedPercent: %s%" % (
                AppConfig.ip, available, percent
            )
            logger.info(smsg)
            send_msg(smsg)
        time.sleep(180)
