# -*- coding:utf-8 -*-
"""
标准字典包括一个setdefault()方法,该方法被用来获取一个值,如果这个值不存在则建立一个默认值,与之相反,初始化容器时defaultdict会让调用者
提前指定默认值.
"""
import collections


def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo ->', d['foo'])
print('bar ->', d['bar'])
