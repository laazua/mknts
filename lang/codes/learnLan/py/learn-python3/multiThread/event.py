# -*- coding: utf-8 -*-

"""
Event对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生
"""
from threading import Thread, Event
import time

evt = Event()

def do_task(evt):
    print("task start")
    evt.set()
    for i in range(10):
        print("hahaha", i)
        time.sleep(2)

    
if __name__ == "__main__":
    t = Thread(target=do_task, args=(evt,))
    t.start()
    evt.wait()
    print("task running")