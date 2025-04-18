# -*- coding:utf-8 -*-
"""
访问堆内容:
    一旦堆已经被正确组织,使用heappop()可以删除有最小值的元素
"""

import heapq
from .heapq_showtree import show_tree
from .heapq_heapdata import data


print('rnado,: ', data)
heapq.heapify(data)
print('heapified: ')
show_tree(data)

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop {:>3}:'.format(smallest))
    show_tree(data)
