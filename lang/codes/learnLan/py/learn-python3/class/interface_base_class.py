# -*- coding: utf-8 -*-
"""
使用abc模块轻松定义抽象基类(接口)
抽象基类的一个特点是它不能直接实例化.其目的就是让别的类继承它并实现特定的抽象方法
主要用途是在代码中检查某些类是否为特定类型,实现了特定接口.
"""
from abc import ABCMeta, abstractmethod
import io
import collections


class IStream(metaclass=ABCMeta):
    """抽象基类(接口)定义"""

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    """继承抽象基类实现特定的方法"""

    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    """用途: 在代码中检查某些类是否为特定类型,实现了特定接口"""

    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


# 除了继承,还可以通过注册方式来让某个类实现抽象基类
# 注册内置的I/O类来实现接口
IStream.register(io.IOBase)

# 打开一个文件并检查它的类型
with open('foo.txt') as fd:
    isinstance(fd, IStream)


# @abstractmethod还能注解静态方法, 类方法和properties.只要保证这个注解紧靠在函数定义前.
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


# 使用与定义的抽象类来执行更通用的类型检查
def check_type(x):
    # check if x is a sequence
    if not isinstance(x, collections.Sequence):
        raise TypeError('Expected sequence')

    if not isinstance(x, collections.Size):
        raise TypeError('Excepted, size')

    if not isinstance(x, collections.Mapping):
        raise TypeError('Excepted, map')


