# -*- coding: utf-8 -*-
"""
实现一个类,除了使用__init__方法外,还可以使用其他方法初始化它
"""


import time


class Date:

    def __init__(self, year, month, dayy):
        self.year = year
        self.month = month
        self.day = day

    # 使用类方法定义构造器
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_yday, t.tm_mon, t.tm_mday)


# 定义类时绕过init()函数创建对象
class Time:

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
