# -*- coding: utf-8 -*-
"""
日志记录
"""
import os
import stat
from loguru import logger
from .config import gmdcon


class GmLog:
    def __init__(self):
        self.log_file = gmdcon.gmd_path + '/logs/app.log'
        self.log_dir = gmdcon.gmd_path + '/logs/'
        
    def writelog(self, data):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir, stat.S_IRWXU)
        # 禁用控制台输出
        logger.remove(handler_id=None)
        logger.add(self.log_file, rotation='00:00')
        # logger.debug(data)
        logger.info(data)

    def errlog(self, data):
        pass


gmdlog = GmLog()