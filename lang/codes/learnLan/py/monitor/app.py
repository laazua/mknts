# -*- coding: utf-8 -*-
"""
监控系统资源使用情况
"""

import os
import sys
import signal
import getopt
import logging
from concurrent.futures import ThreadPoolExecutor
from config import AppConfig
from applibs import (
    disk, load, mem, net, user
)


def modules_pools():
    modules = [disk, load, mem, net, user]
    with ThreadPoolExecutor(max_workers=len(modules)) as executor:
        for module in modules:
            executor.submit(module.run)


def create_daemon():
    """
    创建程序的守护进程
    :return:
    """
    try:
        if os.fork() > 0:
            sys.exit(0)
    except OSError as e:
        raise e

    os.chdir(AppConfig.app_path)
    os.umask(0)
    os.setsid()

    try:
        pid = os.fork()
        if pid > 0:
            with open(AppConfig.pid_file, "w") as fd:
                fd.write(str(pid))
            sys.exit(0)
    except OSError as e:
        raise e

    modules_pools()


def start_app():
    """
    启动app程序
    :return:
    """
    with open(AppConfig.pid_file, "r") as fd:
        pid = fd.read()
        if pid:
            print("app is running...")
            sys.exit(0)
        else:
            create_daemon()


def stop_app():
    """
    关闭app程序
    :return:
    """
    if os.path.exists(AppConfig.pid_file):
        with open(AppConfig.pid_file, "r+") as fd:
            pid = fd.read()
            if pid:
                print(pid)
                fd.seek(0)
                fd.truncate()
                os.kill(int(pid.strip()), signal.SIGKILL)
            else:
                print("app is stopped...")


def print_help():
    """
    程序的帮助信息
    :param: None
    :return: None
    """
    print("""
        Usage: python3 app.py -s [start|stop]
        -h      help message.
        -s      [start|stop].
    """)
    sys.exit(0)


def main():
    opts, args = getopt.getopt(sys.argv[1:], "s:h")
    for op, value in opts:
        if op == "-h":
            print_help()
        if op == "-s":
            if value == "start":
                start_app()
            elif value == "stop":
                stop_app()
            else:
                print("Unknow command {!r}".format(value))


if __name__ == "__main__":
    # 日志记录
    formatter = "%(asctime)s - %(levelname)s - %(message)s"
    date = "%Y-%m-%d %H:%M:%S %p"
    logging.basicConfig(filename='logs/app.log', filemode="a", level=logging.DEBUG, format=formatter, datefmt=date)

    main()
