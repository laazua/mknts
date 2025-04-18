# -*- coding:utf-8 -*-
"""
堆创建
"""
import heapq
from .heapq_showtree import show_tree
from .heapq_heapdata import data


heap = []
print('random: ', data)

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
