# -*- coding:utf-8 -*-
"""
heapq还包括两个检查可迭代对象的函数,可以查找其中包含的最大或最小值的范围
"""

import heapq
from .heapq_heapdata import data


print('all        :', data)
print('3 largest  :', heapq.nlargest(3, data))
print('from sort  :', list(reversed(sorted(data)[-3:])))
print('3 smallest :', heapq.nsmallest(3, data))
print('from sort  :', sorted(data)[:3])
