# -*- coding: utf-8 -*-
"""
当想用有很多方法来扩展其他类的功能并且这些类没有继承关系时,不能简单的将这些方法放入基类来被其它类继承
"""
from collections import defaultdict


# 下面定义了三个混入类

class LoggedMappingMixin:
    """
    add logging to get/set/delete operations for debugging.
    """

    # 混入类没有属性, 设置__slots__等于一个空元组
    __slots__ = ()

    def __getitem__(self, item):
        print('getting' + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    """only allow a key to be set once."""

    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    """restrict keys to strings only"""

    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__seitem__(key, value)


# 以上三个类不能单独使用,不能被实例化;可以与其他对象共同被继承混合使用


class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


# 用类装饰器实现混入类
def logged_mapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__

    return cls


@logged_mapping
class LoggedList(list):
    pass


if __name__ == '__main__':
    d = LoggedDict()
    d[1] = 'a'
    d[2] = 'b'
    for k, v in d.items():
        print(k, v)
    print('-------')
    b = SetOnceDefaultDict(list)
    b['x'].append(2)
    b['x'].append(3)
    for k, v in b.items():
        print(k, v)

    print('-------')
    c = LoggedList()
    c.append(1)
    c.append(2)
    print(c)
