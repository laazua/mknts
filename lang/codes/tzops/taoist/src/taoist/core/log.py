"""
日志
"""

import logging
from uvicorn.config import LOGGING_CONFIG

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# 复制默认配置
UVICORN_CONFIG = LOGGING_CONFIG.copy()

# 修改格式
UVICORN_CONFIG["formatters"]["default"]["fmt"] = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
UVICORN_CONFIG["formatters"]["default"]["datefmt"] = "%Y-%m-%d %H:%M:%S"

# 应用到access日志记录器
UVICORN_CONFIG["loggers"]["uvicorn.access"]["propagate"] = True
UVICORN_CONFIG["loggers"]["uvicorn.access"]["handlers"] = ["default"]
UVICORN_CONFIG["loggers"]["uvicorn.access"]["level"] = "INFO"

# 应用到error日志记录器
UVICORN_CONFIG["loggers"]["uvicorn.error"]["propagate"] = False
UVICORN_CONFIG["loggers"]["uvicorn.error"]["handlers"] = ["default"]
UVICORN_CONFIG["loggers"]["uvicorn.error"]["level"] = "ERROR"


class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"  # 重置颜色
