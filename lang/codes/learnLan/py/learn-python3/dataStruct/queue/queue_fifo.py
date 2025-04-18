# -*-coding:utf-8 -*-
"""
Queue类实现了一个基本的先进先出容器,使用put()将元素增加到这个序列的一端,使用get()从另一端删除.
"""

import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
