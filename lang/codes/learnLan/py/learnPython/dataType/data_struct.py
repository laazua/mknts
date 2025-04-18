# -*- coding: utf-8 -*-
"""
python中的数据结构.
注意各种数据结构的常用方法的使用以及推导式的使用
"""

def generator_factory():
    """
    生成器函数
    """
    i = 0
    while i < 10:
        yield i
        i += 1


def main():
    # 列表, 可变
    list_1 = list()
    list_2 = []
    list_3 = list_1[:]

    # 元祖, 不可变
    tuple_1 = tuple()
    tuple_2 = (1,)
    tuple_3 = 1, 2

    # 字典, k-v
    dict_1 = dict()
    dict_2 = {}

    # 集合, 无序，不重复
    set_1 = set()
    set_2 = {1, 2}

    # 迭代器
    # 迭代器对象 = iter(可迭代对象)
    # next(迭代器对象)   最后抛出StopIteration异常
    # 迭代器内部实现了一个__next__()函数

    # 生成器,可以用for循环取出元素
    gen_1 = (i for i in range(10))  # <generator object <genexpr> at 0x1dcae60b0>
    # yield关键字
    gen_2 = generator_factory()
    for i in gen_2:
        print(i)    


if __name__ == "__main__":
    main()