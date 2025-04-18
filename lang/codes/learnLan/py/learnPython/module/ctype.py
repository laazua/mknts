# -*- coding:utf-8 -*-
"""
python调用c库
  c程序编译成动态连接库:
    gcc -fpic -shared digui.c -o test.so
"""

from ctypes import *


so = CDLL(./test.so)

so.test()
