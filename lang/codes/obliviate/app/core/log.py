"""
自定义日志处理器
"""

import logging
import pathlib

import app.core.config as setting


# 自定义日志配置
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'access': {
            'format': '%(asctime)s %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'access': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'access',
        },
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        },
        'uvicorn.access': {
            'level': 'INFO',
            'handlers': ['access'],
            'propagate': False,
        },
    },
}

# 映射env日志级别
_log_level = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}


# 自定义日志配置
def _get_logger():
    logger = logging.getLogger('app_logger')
    logger.setLevel(_log_level[setting.APP_LOG_LEVEL])
    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    if pathlib.Path('logs').exists() is False:
        pathlib.Path('logs').mkdir(parents=True, exist_ok=True)
    # 创建控制台处理器并设置日志格式
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # 文件日志切割,按日期切割日志
    rotate_handler = logging.handlers.TimedRotatingFileHandler(
        'logs/app.log', when='midnight', interval=1, backupCount=7
    )
    rotate_handler.setFormatter(formatter)
    logger.addHandler(rotate_handler)
    # 按文件大小切割日志
    # size_handler = logging.handlers.RotatingFileHandler(
    #     'logs/app.log', maxBytes=1024 * 1024 * 5, backupCount=7
    # )
    # size_handler.setFormatter(formatter)
    # logger.addHandler(size_handler)

    return logger


logger = _get_logger()