# -*- coding: utf-8 -*-

"""
tuple的使用
支持索引和切片操作，属于序列数据类型
元組属于不可更改数据类型, 即单独给元組中的元素赋值是不允许的
"""


def test_tuple() -> None:
    """
    元組测试
    """
    t = 1, 2 ,3
    print(t)

    # 空元組
    t_empty = ()
    one_tuple = (1,)