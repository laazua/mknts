# -*- utf-8 -*-
"""
循环队列
"""


from queue import Queue
import threading, time

pQueue = Queue()

class TestQueue(threading.Thread):
    def __init__(self, pQueue):
        threading.Thread.__init__(self)
        self._pQueue = pQueue

    def run(self):
        while True:
            if self._pQueue.qsize() > 0:
                try:
                    data = self._pQueue.get()
                    print(data)
                    time.sleep(10)
                except:
                    print("empty pQueue")
            else:
                add_data()

def add_data():
    alist = [1 ,2, 3, 4, 5]
    for i in alist:
        pQueue.put(i)


if __name__ == '__main__':

    add_data()

    for i in range(5):
        TestQueue(pQueue).start()

