"""
使用logging记录日志
logging模块化设计,包含一下4种组件:
  - Logger: 记录器,提供应用程序代码能直接使用的接口
  - Handlers: 处理器,将记录器产生的日志发送至目的地
  - Filters: 过滤器,提供更好粒度的控制,决定哪些日志被输出
  - Formatters: 格式化器,设置日志内容的组成结构和消息字段

logging日志记录工作流程:
  - 创建一个logger并设置默认日志等级-> 创建Handler -> 设置日志等级 -> 创建formatter -> 用formatter渲染所有的Handler -> 将所有的Handler加入logger内 -> 程序调用logger
"""
import logging

# 创建logger记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建Handler处理器
file_handler = logging.FileHandler(filename="app.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# formatter格式
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# formatter渲染handler
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将handler加入logger内
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 程序调用logger
logger.info("xxx")