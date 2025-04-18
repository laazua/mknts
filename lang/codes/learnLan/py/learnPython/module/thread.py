# -*- coding: utf-8 -*-
"""
多线程
"""
import time
import threading
from threading import Lock
from threading import Thread
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor


def test():
    for i in range(10):
        print("haha-{}".format(i))
        time.sleep(2)


class TestThread(Thread):
    def __init__(self):
        super().__init__()  # 必须写

    def run(self):
        """重写Thread的run()方法"""
        for i in range(10):
            print("hehe-{}".format(i))
            time.sleep(2)


# 实例化锁对象
# lock = Lock()
# 获取锁,未获取到会阻塞程序,直到获取到锁才会往下执行
# lock.acquire()
# 释放锁,归还锁,其他人可以拿去用了
# lock.release()
# 推荐使用上下文管理器来加锁
# with lock:
#     pass


# 可重如锁Rlock
# rlock = RLock()


# Thread-local状态到已获取锁的存储信息
_local = threading.local()

@contextmanager
def acquire(*locks):
    """锁排序"""
    # 按对象标识符对锁进行排序
    locks = sorted(locks, key=lambda x: id(x))

    # 确保不违反先前获取的锁的锁顺序
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # 获取所有的锁
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 以与获取相反的顺序释放锁
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


if __name__ == "__main__":
    # 函数创建多线程
    t = Thread(target=test)  # 创建一个线程
    t.start()  # 启动子线程

    # 类创建多线程
    T = TestThread()
    T.start()

    # 阻塞子线程，待子线程结束后，再往下执行
    # t.join() 
    # 判断线程是否在执行状态，在执行返回True，否则返回False
    # t.is_alive()
    # t.isAlive()
    # 设置线程是否随主线程退出而退出，默认为False
    # t.daemon = True
    # t.daemon = False
    # 设置线程名
    # t.name = "My-Thread"

    # 线程池
    with ThreadPoolExecutor(5) as pool:
        for i in range(100):
            pool.submit(test)