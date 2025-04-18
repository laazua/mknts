# -*- coding:utf-8 -*-
"""
author: Sseve
"""

import os
import logging

from setting import APP_PATH


class Log:
    def __init__(self, flag='yunwei', log_dir=APP_PATH.join('logs')):
        self.flag = flag
        self.log_dir = log_dir

    def write_log(self):
        logger = logging.getLogger(self.flag)
        logger.setLevel(logging.DEBUG)

        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
