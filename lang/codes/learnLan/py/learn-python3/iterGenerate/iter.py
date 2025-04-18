# -*- coding:utf-8 -*-

"""
可迭代对象:
list, tuple, dict, set, str
generator, 生成器, 带yield的generator function
"""

from collections import Iterable

def test_iter():
    array = [1, 2, 3, 4, 5]
    if isinstance(array, Iterable):
        print("我是可迭代的")