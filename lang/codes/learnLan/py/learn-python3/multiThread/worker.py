# -*- coding:utf-8 -*-


import threading


class Worker(threading.Thread):

    # our workers constructor, note the super() method which is vital
    # if we want this to function properly
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(10):
            print(i)


if __name__ == "__main__":
    ## this initializes 'thread1' as an instance of our Worker Thread
    thread1 = Worker()
    thread1.start()