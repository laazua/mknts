#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading,logging,time,queue
import pd1, pd2

q = queue.Queue()


def thread_function2(name:tuple) -> None:
    logging.info("Thread %s: starting", name)
    while True:
        print("I am thread two qiqiqi")
        time.sleep(2)
        #logging.info("Thread %s: finishing", name)


def thread_function1(name: tuple) -> None:
    logging.info("Thread %s: starting", name)
    while True:
        print("I am thread one hahaha")
        time.sleep(2)

    #logging.info("Thread %s: finishing", name)


class Pthread(threading.Thread):
    def __init__(self, q_input):
        threading.Thread.__init__(self)
        self._q_input = q_input

    def run(self):
        while True:
            if self._q_input.qsize() > 0:
                try:
                    q_job = self._q_input.get()
                    q_job.Run()
                except queue.Empty as e:
                    q_size = 0
            else:
                break


if __name__ == "__main__":

    # 格式输出设定
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    """
    # 方式一
    # 将要执行的各个函数放进队列
    qlist = [thread_function1, thread_function2]
    for i in qlist:
        q.put(i)

    # 从队列中取出要执行的函数,调用threading.Thead()去执行.
    for i in range(len(qlist)):
        x = threading.Thread(target=q.get(), args=(i,))
        x.start()
    """
    # 方式二
    pdlist = ["pd1", "pd2"]     # 配置文件时使用
    q.put(pd1)
    q.put(pd2)

    for i in range(len(pdlist)):
        Pthread(q).start()

    """ 
    logging.info("Main : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main : before running thread")
    x.start()
    logging.info("Main : wait for the thread to finish")
    # x.join()
    logging.info("Main : all done")
    """