# -*- coding:utf-8 -*-
"""
装饰器
"""

def foo():
    pass


def decorator(func):
    # manipulate func
    return func


foo = decorator(foo)    # manually decorate


@decorator
def bar():    # bar() is decorated
    pass