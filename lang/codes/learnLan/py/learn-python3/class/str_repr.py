# -*- coding: utf-8 -*-
"""
给对象实例的打印或显示输出
重新定义类的str()和repr()方法
"""


class Test:
    """给对象实例的打印或显示输出"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # !r格式化代码指明输出使用repr()代替默认的str()
    def __repr__(self):
        return 'Test({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
