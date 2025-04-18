# -*- coding: utf-8 -*-

"""
字典，即映射，键值对集合
支持推导式
"""

def test_dict() -> None:
    """
    测试字典
    """
    # 创建空字典
    d = {}

    d[0] = 'a'
    d[1] = 'b'
    print(d)

    # 循环
    for k, v in d.items():
        print(k, v)


from collections import OrderedDict
import json
def dict_sort():
    """
    在迭代或者序列化字典的时候保持字典的顺序
    OrderedDict()函数会生成一个顺序不会改变的字典
    """
    md = OrderedDict()
    md[1] = "a"
    md[2] = "b"
    md[3] = "c"
    for key in md:
        print(key,md[key])
    
    print(json.dumps(md))


if __name__ == "__main__":
    test_dict()
    dict_sort()