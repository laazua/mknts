import os
import logging
import datetime
from logging import handlers
from app.config import cfg


def _get_logger(level: str) -> logging.Logger:
    log_path = os.path.join(os.path.dirname(__file__), "../../../logs")
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    filename = f"{log_path}/zservant.log"

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
        filename=filename,
        when="midnight",
        interval=1,
        backupCount=7,
        atTime=datetime.time(0, 0, 0, 0))
    formatter = "[%(asctime)s - %(levelname)s - %(lineno)s] %(message)s"
    handler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(handler)

    return logger


logger = _get_logger(cfg.get("app", "logLevel"))
