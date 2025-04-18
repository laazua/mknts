# -*- coding: utf-8 -*-
"""
collections定义了很多抽象基类,可以继承它里面的基类实现各种定制的类型
"""
import collections
import bisect


class SortedItems(collections.Sequence):
    """实现一个Sequence,必须实现基类中所有的抽象方法"""
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # 需要实现的抽象方法
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # 往右边添加元素
    def add(self, item):
        bisect.insort(self._items, item)    # bisect模块,在排序表中插入元素的高效方式,可以保证元素插入后还保持顺序


class Items(collections.MutableSequence):

    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # 需要实现的基类中的抽象方法
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __delitem__(self, index):
        print('deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('len')
        return len(self._items)


# 创建Items实例,它支持几乎所有核心列表的方法
