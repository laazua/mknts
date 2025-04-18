# -*- coding: utf-8 -*-
"""
任何时候定义装饰器的时候,都应该使用functools库中的@wraps装饰器来注解底层包装函数.
装饰器函数中不使用@wraps会丢失所有有用的信息
"""
import time
from functools import wraps


def time_this(func):
    """装饰器函数"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@time_this
def count_down(n):
    """counts down"""

    while n > 0:
        n -= 1


