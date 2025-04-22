### logging

- **示例**
```python
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


logging.debug("debug message")
logging.info("info message")
logging.fatal("fatal message")
logging.error("error message")
```

- **logger**
```python
import logging


# 获取一个日志记录器
logger = logging.getLogger("__name__")
# 设置日志级别
logger.setLevel(logging.DEBUG)

# 创建控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# 创建一个文本文件处理器
textfile_handler = logging.FileHandler("app.log")
textfile_handler.setLevel(logging.INFO)

# 格式化日志输出
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
textfile_handler.setFormatter(formatter)

# 添加处理器到logger日志记录器
logger.addHandler(console_handler)
logger.addHandler(textfile_handler)


class LevelFilter(logging.Filter):
    """
    过滤日志级别: 只输出ERROR级别日志
    """

    def filter(self, record):
        """重写父类的filter()方法"""
        return record.levelname == "ERROR"


logger.addFilter(LevelFilter())

logger.debug("debug message")
logger.info("info message")
logger.fatal("fatal message")
logger.error("error message")
```