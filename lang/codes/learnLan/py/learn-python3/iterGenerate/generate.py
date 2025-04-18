# -*- coding:utf-8 -*-

"""
生成器: 可以使用next()方法调用下一个元素的对象
"""

import types

def test_generate():
    g = (x*2 for x in range(6))
    if isinstance(g, types.GeneratorType):
        print("我是一个生成器")
    else:
        print("aaa")

    for i in g:
        print(i)


def fib(max):
    """
    生成器函数
    """
    a, b = 0, 1
    for i in range(max):
        yield b
        a, b = b, a + b
    

def test_fib():
    f = fib(5)
    if isinstance(f, types.GeneratorType):
        print("我是生成器函数")

    for i in fib(6):
        print(i)


if __name__ == "__main__":
    #test_generate()
    test_fib()
    