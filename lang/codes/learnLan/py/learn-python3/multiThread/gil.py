# -*- coding:utf-8 -*-

"""
GIL缺点优化方案
"""

from multiprocessing import Pool


# 原始代码,(cpu密集型任务)
def some_work(args):
    # some code
    return result


# 调用上面函数some_work()的线程
def some_thread():
    while True:
        # some code
        r = some_work(args)


# 修改后代码(进程池)
pool = None

def some_works(args):
    # some code
    return result


def some_threads():
    while True:
        # some code
        r = pool.apply(some_works, (args))


if __name__ == '__main__':
    pool = Pool()