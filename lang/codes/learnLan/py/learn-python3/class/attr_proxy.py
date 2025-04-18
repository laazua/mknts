# -*- coding: utf-8 -*-
"""
将某个实例的属性访问代理到另一个实例中去,目的可能是作为继承的一个替代方法或者实现代理模式
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """简单代理,当需要代理的方法不多是使用此方法"""
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # 实例_a内部的一个代理
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2:
    """使用__getattr__的代理,代理的方法比较多的时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # 公开类A上定义的所有方法
    def __getattr__(self, item):
        return getattr(self._a.item)
