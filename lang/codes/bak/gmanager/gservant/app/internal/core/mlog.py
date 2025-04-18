import os
import logging
import datetime
from logging import handlers


def _get_logger() -> logging.Logger:
    log_path = os.path.join(os.getcwd(), ".") + "/logs"
    if not os.path.exists(log_path):
        os.makedirs(log_path, 755)
    filename = os.path.abspath(
        log_path + "/gservant.log")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = handlers.TimedRotatingFileHandler(filename=filename, 
                    when='midnight', interval=1, backupCount=7, 
                    atTime=datetime.time(0, 0, 0, 0))
    formatter = "[%(asctime)s - %(levelname)s - %(module)s - %(filename)s - %(lineno)s]  %(message)s"
    handler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(handler)

    return logger


logger = _get_logger()
