### daemon

- **守护进程**
1. 代码
```python
import os
import sys
import time


def daemon():
    try:
        if os.fork() > 0:
            # 父进程退出
            os._exit(0)
    except OSError as e:
        print(f"fork #1 failed: {e.errno} {e.strerror}")
        os._exit(-1)

    # 创建新的会话，脱离终端
    os.chdir("/")
    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            # 父进程退出
            with open("/var/run/testdaemon/daemon.pid", "w") as fd_pid:
                fd_pid.write(str(pid))
            os._exit(0)
    except OSError as e:
        print(f"fork #2 failed: {e.errno} {e.strerror}")
        os._exit(-2)

    # 重定向标准io到/dev/null
    sys.stdout.flush()
    sys.stderr.flush()
    try:
        si = open("/dev/null", "r")
        so = open("/dev/null", "a+")
        se = open("/dev/null", "a+")
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())
        si.close()
        so.close()
        se.close()
    except Exception as e:
        print(f"重定向失败: {e}")
        os._exit(-3)

    # 进入子进程逻辑
    run()


def run():
    """模拟程序逻辑"""
    try:
        with open("app.log", "w") as fd:
            while True:
                fd.write(f"{time.time()} this is a test\n")
                time.sleep(1)
    except IOError as e:
        print(f"程序出错: {e.strerror}")


if __name__ == "__main__":
    if platform.system() == "Linux":
        daemon()

```

2. 环境
```bash
sudo chown user:user /var/run/testdaemon/
```