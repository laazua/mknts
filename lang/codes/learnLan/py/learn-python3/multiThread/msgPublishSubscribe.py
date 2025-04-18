# -*- coding:utf-8 -*-
"""
问题:你有一个基于线程通信的程序，想让它们实现发布/订阅模式的消息通信。
解决方案:要实现发布/订阅的消息通信模式， 你通常要引入一个单独的“交换机”或“网关”对象作为所有消息的中介。 
        也就是说，不直接将消息从一个任务发送到另一个，而是将其发送给交换机， 然后由交换机将它发送给一个或多个被关联任务.
"""

from collections import defaultdict

class Exchange:
    """
    交换机
    """
    def __init__(self):
        '''
        初始化一个集合,放置不重复元素
        '''
        self._subscribers = set()

    def attch(self, task):
        '''
        往集合中添加元素
        '''
        self._subscribers.add(task)

    def detach(self, task):
        '''
        从集合中删除元素
        '''
        self._subscribers.remove(task)

    def send(self, msg):
        for sub in self._subscribers:
            sub.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        pass

if __name__ == '__main__':
    task_a = Task()
    task_b = Task()

    #获取exchage
    exc = get_exchange('name')
    
    #订阅消息
    exc.attch(task_a)
    exc.attch(task_b)

    #发送消息
    exc.send("hello")
    exc.send("world")

    #解绑订阅
    exc.detach(task_a)
    exc.detach(task_b)