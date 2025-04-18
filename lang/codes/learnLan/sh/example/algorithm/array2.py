#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
定义一个int型的数组,包含10个元素,分别赋值1--10,然后将数组中的元素都向前移一个位置,
即, a[0]=a[1], a[1]=a[2], ...最后一个元素的值是第一个元素的值,然后输出这个数组
"""

def ahead_one() -> list:
    """
    :return: a
    """
    a = [ i for i in range(10)]
    b = a.pop(0)
    print(b)
    a.append(b)
    return a


if __name__ == '__main__':
    print(ahead_one())