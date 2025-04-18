# -*- coding: utf-8 -*-
"""
抽象类不能被实例化,用途检查某些类是否为特定类型,实现了特定方法
"""

from abc import ABCMeta, abstractmethod


class InterfaceAbstract(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

# t = InterfaceAbstract()  会报错
# InterfaceAbstract()类中的方法全部未实现,则InterfaceAbstract()视为接口类
# InterfaceAbstract()类中的方法部分未实现,则InterfaceAbstract()视为抽象类