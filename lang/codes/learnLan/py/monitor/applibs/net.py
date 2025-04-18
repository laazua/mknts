# -*- coding: utf-8 -*-
"""
监控网络流量
"""

import time
import logging
from psutil import net_io_counters
from .sendmsg import send_msg
from config import AppConfig


def count_mbps():
    """
    计数mbps out/in情况
    """
    net_mbps = {}
    first_mbps = net_io_counters(pernic=True)
    time.sleep(30)
    second_mbps = net_io_counters(pernic=True)
    for dev in second_mbps:
        if dev == AppConfig.inet:
            send_mbps = (second_mbps[dev].bytes_sent - first_mbps[dev].bytes_sent) * 8 / 30 / ((2<<9)**2)
            recv_mbps = (second_mbps[dev].bytes_recv - first_mbps[dev].bytes_recv) * 8 / 30 / ((2<<9)**2)
            send_mbps_round = str(round(send_mbps, 2))
            recv_mbps_round = str(round(recv_mbps, 2))
            net_mbps[dev] = {"send_mbps": send_mbps_round, "recv_mbps": recv_mbps_round}

    return net_mbps


def run():
    logger = logging.getLogger('app')
    logger.info("start monitor net...")
    while True:
        current_net = count_mbps()
        for dev in current_net:
            send_mbps = float(current_net[dev]["send_mbps"])
            recv_mbps = float(current_net[dev]["recv_mbps"])
            if send_mbps > AppConfig.net_out or recv_mbps > AppConfig.net_in:
                smsg = "IP: %s, out: %sMbps, in: %sMbps" % (
                    AppConfig.ip, send_mbps, recv_mbps
                )
                logger.info(smsg)
                send_msg(smsg)
        time.sleep(180)
