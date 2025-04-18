# -*- conding: utf-8 -*-
"""
描述器:一个描述器就是实现了三个核心的属性访问操作(get(),set(),delete())的类
可以通过描述器类的形式来定义一个全新的实例属性的功能
描述器可以实现大部分python类特性中的底层魔法,包括@classmethod, @staticmethod, @property, slots特性
"""


class Integer:
    """描述器定义"""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    """
    描述器使用:
    所有对描述器属性(x, y)的访问会被get(),set(),delete()方法捕获到
    """
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
