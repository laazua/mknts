# -*- coding:utf-8 -*-
"""
对于小数据集,将多个有序序列合并到一个新序列很容易.
list(sorted(itertools.cain(*data))).
对于较大数据集,该方法会占用大量内存,merge()不是对整个合并后的序列排序,而是使用一个堆一次一个元素地生成一个新序列,利用固定大小的内存确定
下一个元素.
"""

import heapq
import random


random.seed(2021)

data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for i, d in enumerate(data):
    print('{}: {}'.format(i, d))

print('\nMerged:')
for i in heapq.merge(*data):
    print(i, end=' ')
print()
