"""
date: 2024-01-05
"""
import os
import logging
import datetime
import logging.handlers as handlers

from src.count_es.config import config


def _get_logger(level, stdout):
    """日志记录"""
    logger = logging.getLogger(__name__)
    if level == logging.NOTSET:
        logger.setLevel(logging.NOTSET)
    elif level == logging.DEBUG:
        logger.setLevel(logging.DEBUG)
    elif level == logging.INFO:
        logger.setLevel(logging.INFO)
    elif level == logging.WARN:
        logger.setLevel(logging.WARN)
    elif level == logging.FATAL:
        logger.setLevel(logging.FATAL)
    else:
        logger.setLevel(logging.INFO)
    formatter = "[%(asctime)s - %(levelname)s - %(lineno)s] %(message)s"
    if not stdout:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        fileHandler = handlers.TimedRotatingFileHandler(
            filename="logs/app.log", when="midnight", interval=1,
            backupCount=7, atTime=datetime.time(0, 0, 0, 0)
        )
        fileHandler.setFormatter(logging.Formatter(formatter))
        logger.addHandler(fileHandler)
    else:
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(logging.Formatter(formatter))
        logger.addHandler(streamHandler)

    return logger


Logger = _get_logger(config.get("app", "loglevel"), config.getboolean("app", "logstdout"))
