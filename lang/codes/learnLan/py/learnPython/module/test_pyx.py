# -*- coding:utf-8 -*-
"""
python模块转换成c库：
  - 将模块文件修改为.pyx类型: mv test.py test.pyx
  - 编写setup.py脚本
  - 运行脚本:python setup.py build_ext --inplace
    
setup.py:
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='any',
    ext_modules=cythonize(
        [
            "test.pyx"
        ]
    )
)
"""
