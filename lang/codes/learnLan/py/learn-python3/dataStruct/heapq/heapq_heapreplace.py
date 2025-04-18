# -*- coding:utf-8 -*-
"""
删除现有元素并替换为新值,使用heapreplace()
"""

import heapq
from .heapq_heapdata import data
from .heapq_showtree import show_tree


heapq.heapify(data)
print('start: ')
show_tree(data)
for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))
    show_tree(data)
