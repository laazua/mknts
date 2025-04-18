"""
所有实现模块放在此包下
"""
import functools
from typing import Callable

from lanpy.iface import ICar


def decorator_class(cls):
    """
    类装饰器
    :param cls: 被装饰的类
    :return:
    """
    print("class name: ", cls.__name__)
    return cls


def decorator_method(item: str) -> Callable:
    """
    带参数的类方法装饰器
    :param item: 指明是哪种物种, person or animal
    """
    def inner_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """
            :param self: 被装饰实例
            :param args: 被装饰实例方法的位置参数
            :param kwargs: 被装饰实例方法的关键字参数
            :return: None
            """
            if item == "person":
                print("Person Behaviour")
            if item == "animal":
                print("Animal Behaviour")
            func(self, *args, **kwargs)
        return wrapper
    return inner_decorator


@decorator_class
class Person:
    """
    这是一个Person实现示例, 实现Species协议
    """
    def __init__(self, name):
        self.name = name

    @decorator_method("person")
    def sing(self):
        print(self.name, "is sing ...")

    @decorator_method("person")
    def running(self):
        print(self.name, "is running ...")


@decorator_class
class Animal:
    """
    这是一个Animal实现示例, 实现Species协议
    """
    def __init__(self, name):
        self.name = name

    @decorator_method("animal")
    def sing(self):
        print(self.name, "is sing ...")

    @decorator_method("animal")
    def running(self):
        print(self.name, "is running ...")


class Benz(ICar):
    """
    这是一个Benz实现示例,实现ICar接口,必须强制实现
    """
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(self.name, "is running ...")


class Bmw(ICar):
    """
    这是一个Bmw实现示例,实现ICar接口,必须强制实现
    """
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(self.name, "is running ...")