import logging
from logging import config

# 配置文件的方式处理日志
config.fileConfig("logging.conf")

root_logger = logging.getLogger()
root_logger.debug("root log")

logger = logging.getLogger("applog")
logger.debug("app log")