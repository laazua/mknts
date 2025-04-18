# -*- coding: utf-8 -*-

"""
python中变量赋值是将对象的引用地址给变量,类似c语言中的指针
x, y = 1, 2
x , y = y, x
"""

def test_value() -> None:
    a = 1
    b = a   # 将a中对象的引用地址给b
    print("a = {}".format(a))
    print("b = {}".format(b))


def test_number() -> None:
    """
    operator: + - * / // % **
    """
    a = 1
    b = 2.5
    print(a + b)


def test_string() -> None:
    """
    (''),(""),('''strings'''),(\"\"\"sstrings\"\"\")
    operator: + * [:]
    """
    str0 = "fjakdljdjhfauefaen"
    str1 = str0 * 3
    str2 = str0[:-1]
    print(str0, str1, str2)



def test_list() -> None:
    """
    支持列表推导式
    a = [] (a = list() 
    operator: + *  [:]
    """
    a = [1, 2, 6]
    b = [5, 7, 8]
    print(a + b)


def test_tuple():
    """
    a = (1,)
    b = 1, 2, 5
    """

def test_set():
    """
    集合中元素不重复且无序
    支持列表推到式
    a = {'aa', 'bb', 'cc'}
    b = set("adfad") == {a, d, f} 
    """


def test_dict():
    """
    a = dict([('a', 1), ('b', 2), ('c', 3)])
    b = {1: 'aa', 2: 'bb', 3: 'cc'}
    """
    

if __name__ == "__main__":
    test_list()