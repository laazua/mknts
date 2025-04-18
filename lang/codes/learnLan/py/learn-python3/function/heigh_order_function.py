# -*- coding: utf-8 -*-

"""
高阶函数: 把函数本身作为参数传递给另一个函数当作参数
把函数赋值给一个变量,即在内存地址中给函数增加了一个引用(使一个变量指向该函数在内存中的地址)

函数扩展功能模块: functools
"""


def test_function1(x, y, f):
    """
    函数作为参数
    """
    return f(x) + f(y)


def test_function2(x, y):
    """
    函数作为返回值
    """
    def r_func():
        return x + y
    
    return r_func


def test_lambda(x):
    """
    匿名函数
    """
    return lambda x: x * 2


def decorator(func):
    """
    装饰器函数
    """
    def wrapper(*args, **kw):
        print("我是个装饰器,我装饰: {}()".format(func.__name__))
        return func(*args, **kw)
    return wrapper

@decorator
def test_decorator():
    """
    把@decorator放到test_decorator()函数定义处,等价于:
    test_decorator = decorater(test_decorator)
    """
    print("我被decorator函数装饰")


if __name__ == '__main__':
    f = abs     #将函数赋值给一个变量
    res = test_function1(-10, 50, f)
    print(res)
    
    print("==========")

    r = test_function2(1, 2)
    print(r)
    print(r())

    print("==========")
    test_decorator()