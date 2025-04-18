# -*- coding:utf8 -*-
"""
如果输入URL包含多余的部分,那么重新构造的URL可能会将其去除
"""

from urllib.parse import urlunparse, urlparse


original = 'http://netloc/path;?#'

print('ORIG        : ', original)
parsed = urlparse(original)
print('PARSED:     : ', type(parsed), parsed)
t = parsed[:]
print('TUPLE        : ', type(t), t)
print('NEW          : ', urlunparse(t))
