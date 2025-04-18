# -*- coding: utf-8 -*-
import functools


def test_partial(a: str, b: int):
    print(a, b)


class TestPartial:
    def __init__(self):
        pass

    m = functools.partialmethod(test_partial)


@functools.lru_cache(maxsize=10)
def reduce(a: int, b: int):
    return a * b


@functools.singledispatch
def test_singiledispath(arg):
    print(arg)


@test_singiledispath.register(int)
def test_int(arg: int):
    print("test_int: {}".format(arg))


@test_singiledispath.register(list)
def test_list(arg: list):
    for i in arg:
        print(" {}".format(i))


if __name__ == "__main__":
    # functools.partial()返回一个可调用对象
    p = functools.partial(test_partial)
    p(100, 200)

    # functools.partialmethod()返回一个可调用方法
    t = TestPartial()
    t.m(200)

    # functools装饰器

    # cache
    for a in [1,2,3]:
        for b in [1,2,3]:
            print(reduce(a, b), end=' ')
    
    # 泛型函数
    test_singiledispath("test")
    test_singiledispath(12)
    test_singiledispath(5.5)
    test_singiledispath([1,2,3])
   