#!/usr/bin/env python3
#_-*- coding:utf-8 -*-
"""
从一个线程往另一个线程发送数据最安全的方式是，使用队列(queue)
创建一个被多个线程共享的Queue对象，使用put()和get()等方法操作队列。
"""
from queue import Queue
from threading import Thread

Qobject = Queue()
#产生数据的线程
def producer(Qobject):
    data = 0
    while True:
        data = data + 1
        Qobject.put(data)


#使用数据的线程
def consumer(Qobject):
    data = Qobject.get()
    print(data)


if __name__ == '__main__':
    t1 = Thread(target=producer, args=(Qobject,))
    t2 = Thread(target=consumer, args=(Qobject,))
    t1.start()
    t2.start()
