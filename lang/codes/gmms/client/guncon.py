# guncon.py
import os
import sys
import multiprocessing

# address
bind = "0.0.0.0:8888"

# 超时时间
timeout = 40

# 并行工作进程
workers = multiprocessing.cpu_count() * 2 + 1

# 每个进程开启的线程数量
threads = 4

# 服务器在pending状态的最大连接数量
backlog = 2048

worker_class = "uvicorn.workers.UvicornWorker"

# 客户端最大连接数量
work_connections = 1000

daemon = True

logleve = "debug"
pidfile = "app.pid"
accesslog = "log/gun-access.log"
errorlog = "log/gun-error.log"

chdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append("/home/gamecpp/fpvirtual/lib64/python3.9/site-packages/")
sys.path.append("/home/gamecpp/fpvirtual/lib/python3.9/site-packages/")