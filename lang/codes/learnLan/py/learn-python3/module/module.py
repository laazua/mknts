# -*- coding: utf-8 -*-

"""
模块是包含python定义和语句并且以.py结尾文件. 如test.py,即为一个文件，模块名为test（作为一个字符串),可以通过全局变量__name__的值获得
每个模块都有自己的似有符号列表,该表用作模块中的所有函数的全局符号列表
模块搜索路径：内置模块 -> sys.path
不建议使用from test_module import *的方式导入模块这样有个能会覆盖掉一些自己定义的东西
import test_module as test
"""


from test_module import fib, fib2


def test() -> None:
    """
    test
    """
    fib(5)
    fib2(6)


if __name__ == "__main__":
    test()