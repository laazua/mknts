# -*- coding:utf-8 -*-
"""
如果数据已经在内存中,那么使用heapify()原地重新组织列表中的元素会更加高效
"""

import heapq
from .heapq_showtree import show_tree
from .heapq_heapdata import data

print('random: ', data)
heapq.heapify(data)
print('heapified: ')
show_tree(data)
