# -*- coding: utf-8 -*-

"""
global语句定义全局变量
nonlocal语句定义外层函数变量
函数是执行特定功能的代码块
函数调用会引入一个新符号表,函数内部所有的变量赋值都存储来该符号表中
函数传参始终传递的是对象引用
当函数没有显式指定返回值时,会默认返回None
每个函数都有自己的私有符号列表,在函数调用时导入
"""


def foo() -> None:
    """
    这是一个示例函数
    """
    print("这是个示例函数")
    x, y = 1, 2
    x, y = y, x
    print(x, y)


def test_args1(prompt: str, ret: int = 4,  rem: str = "ha ha ha") -> None:
    """
    测试 位置参数，关键字参数
    """
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            print(rem)
        if ok in ("n", "no", "none"):
            print(ret)
        if ok:
            break
    print("bye")


def test_args2(name: str, *args: tuple, **kwargs: dict) -> None:
    """
    测试 tuple参数, dict参数
    """
    print(name)
    
    for i in args:
        print(i)

    for kw in kwargs:
        print(kw, ":", kwargs[kw])


def test_lambda(x: int) -> int:
    """
    测试匿名函数
    """
    return lambda x: x + 1


if __name__ == "__main__":
    res = foo()
    print(res)