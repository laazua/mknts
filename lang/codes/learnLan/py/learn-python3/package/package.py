# -*- coding: utf-8 -*-

"""
python中包是一个包含多个python模块的目录(__init__.py文件初始化当前目录为一个python包),如下：
test/
    __init__.py
    test1/
        __init__.py
        test1a.py
        test1b.py
        test1c.py
    test2/
        __init__.py
        test2a.py
        test2b.py
        test2c.py
    test3/
        __init__.py
        test3a.py
        test3b.py
        test3c.py

访问包中的模块方式 A.B 即A包中的B模块,如下：
import test.test1.test1a
from test.test2 import test2c
from test.test3.test3b import test_function

在子包中导入别的自定义模块，在test3a.py中
from ..test2 import test2c
"""