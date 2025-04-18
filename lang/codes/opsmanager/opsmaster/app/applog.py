import os
import logging
import datetime
from logging import handlers
from app import AppConfig


def _get_logger(level: str) -> logging.Logger:
    """日志记录"""
    logpath = os.path.join(
        os.path.dirname(__file__), "../logs"
    )
    if not os.path.exists(logpath):
        os.makedirs(logpath)
    logfile = "{}/opsmaster.log".format(logpath)
    logger = logging.getLogger(__name__)
    match level:
        case "notset":
            logger.setLevel(logging.NOTSET)
        case "debug":
            logger.setLevel(logging.DEBUG)
        case "info":
            logger.setLevel(logging.INFO)
        case "warn":
            logger.setLevel(logging.WARN)
        case "fatal":
            logger.setLevel(logging.FATAL)
        case _:
            logger.setLevel(logging.INFO)
    handler = handlers.TimedRotatingFileHandler(
        filename=logfile, when="midnight", interval=1,
        backupCount=7, atTime=datetime.time(0, 0, 0, 0)
    )
    formatter = "[%(asctime)s - %(levelname)s - %(lineno)s] %(message)s"
    handler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(handler)

    return logger


AppLogger = _get_logger(AppConfig.get("app", "logLevel"))
