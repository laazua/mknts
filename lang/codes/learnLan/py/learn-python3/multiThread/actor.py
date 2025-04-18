# -*- coding:utf-8 -*-
"""
actor就是一个并发执行的任务,只是简单的执行发送给它的消息任务.
响应这些消息时,它可能还会给其它actor发送更进一步的消息,actor
之间的通信是单向异步的,消息发送者不知道消息是什么时候被发送的,
也不会接收到一个消息已被处理的回应或通知.
"""
from queue import Queue
from threading import Thread, Event

#用于关闭的哨兵
class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        """
        发送一个消息给actor
        """
        self._mailbox.put(msg)

    def recv(self):
        """
        接收消息
        """
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        '''
        关闭actor
        '''
        self.send(ActorExit)

    def start(self):
        '''
        开始并发执行
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        '''
        用户自己实现的运行方法
        '''
        while True:
            msg = self.recv()


# actor任务(test)
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('got: ', msg)


if __name__ == '__main__':
    p = PrintActor()
    p.start()
    p.send("hahaha")
    p.send("nihao")
    p.close()
    p.join()