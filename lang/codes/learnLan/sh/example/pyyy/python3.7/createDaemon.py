#/usr/bin/env python3
# coding=utf-8
import os
import sys
import time
import atexit

def create_daemon() -> None:
    """
    create daemon process
    :return:
    """
    try:
        pid = os.fork()
        if pid:
            sys.exit(0)
    except OSError as e:
        print("first fork process" + e)
    #子进程默认继承父进程的工作目录，最好变更到根目录，否则影响文件系统的卸载
    os.chdir("/")
    #子进程默认继承父进程的umask（文件权限掩码），重设为0（完全控制）
    os.umask(0)
    #让子进程成为新的会话组长和进程组长
    os.setsid()

    try:
        ppid = os.fork()
        if ppid:
            sys.exit(0)
    except OSError as e:
        print("second fork process" + e)

    #刷新缓存区
   # sys.stdin.flush()
    sys.stdout.flush()
    sys.stderr.flush()

    """
    #dup2函数原子化地关闭和复制文件描述符，重定向到/dev/null
    with open("/dev/null") as rfd, open("/dev/null") as wfd:
        os.dup2(rfd.fileno(), sys.stdin.fileno())
        os.dup2(wfd.fileno(), sys.stdout.fileno())
        os.dup2(wfd.fileno(), sys.stderr.fileno())
    """
    with open("/var/run/test.pid", "w") as fd:
        fd.write(str(os.getpid()))

    #注册退出函数，进程异常退出时移除pid文件
    atexit.register(os.remove, "/var/run/test.pid")


if __name__ == '__main__':
    create_daemon()
    print("aa")
    while True:
        print("aaa")
        time.sleep(20)