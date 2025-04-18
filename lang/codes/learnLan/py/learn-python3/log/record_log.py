# -*- coding:utf-8 -*-
"""
在程序运行的过程中,时刻记录程序的输出日志是很重要的
"""
import logging
import logging.handlers as handlers
import time


def set_log(log_name: str):

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    # define formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logHandler = handlers.TimedRotatingFileHandler('app.log', when='D', interval=1, backupCount=2)
    logHandler.setLevel(logging.INFO)

    # set logHandler's formatter
    logHandler.setFormatter(formatter)

    logger.addHandler(logHandler)

    return logger


if __name__ == '__main__':
    while True:
        time.sleep(1)
        logger = set_log('app')
        logger.info("ha ha ha")