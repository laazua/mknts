# -*-coding:utf-8 -*-
"""
利用urlunparse()可以将包含串的普通元组重新组合为一个URL
"""

from urllib.parse import urlparse, urlunparse


original = 'http://netloc/path;param?query=arg#frag'
print('ORIG        : ', original)
parsed = urlparse(original)
print('PARSED      : ', type(parsed), parsed)
t = parsed[:]
print('TUPLE       : ', type(t), t)
print('NEW         : ', urlunparse(t))

