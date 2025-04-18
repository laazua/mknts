# -*- coding:utf-8 -*-
"""
与Queue的标准FIFO实现相反,LifoQueue使用了(通常与栈数据结构相关的)后进先出(LIFO,last-in, first-out)顺序.
"""

import queue


q = queue.LifoQueue()

for i in  range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')

print()
