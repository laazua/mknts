# -*- coding:utf-8 -*-
"""
与其他python序列一样,可以采用同样的方式扩展和处理array
"""
import array
import pprint


a = array.array('i', range(3))
print('Initial: ', a)

a.extend(range(3))
print('Extended: ', a)

print('Slice: ',  a[2:5])

print('Iterator: ', list(enumerate(a)))
