# -*- coding: utf-8 -*-
"""
函数, 注意参数位置的顺序
"""
from functools import reduce
from functools import partial
from functools import singledispatch


def test():
    print("this is a test function.")
    # 默认返回None


def need_args(a, b):
    """必须参数,又叫位置参数"""
    print(a, b)


def default_args(a=10):
    """可选参数,又叫默认参数,或关键字参数"""
    print(a)


def variable_args(*args, **kwargs):
    """
    参数可是不定
    args: 是一个元祖
    kwargs: 是一个字典
    """
    print(args, kwargs)


def star_args(a, b, *, c):
    print(a, b, c)


def partial_test():
    """
    偏函数:可以将某个函数的常用参数进行固定，避免每次调用时都要指定
    """
    p = partial(add_tow, b=2)  # 参数b为经常使用的固定值参数
    r = p(3)
    print(r)


def add_tow(a, b):
    return a + b


def deractor(func):
    """
    外部函数与内部函数组成一个闭包环境
    """
    bar = 10
    def wrapper(*args, **kwargs):
        nonlocal bar
        bar += 10
        func(*args, **kwargs)
    return wrapper


@deractor
def test():
    print("aa")


if __name__ == "__main__":
    # r = test()
    # print(r)

    # star_args(1, 2, c=10)

    # 匿名函数
    # a = map(lambda x: x + 1, [1, 2, 3])
    #b = filter(lambda x: x < 2, range(-5, 5))
    # c = reduce(lambda x, y: x + y, [7 ,8, 9])
    # print(a, b, c)

    # partial_test()

    # deractor()()

    test()