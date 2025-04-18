# -*- coding:utf-8 -*-
"""
实际上urlparse()的返回值是基于一个namedtuple, 这是tuple的一个子类. 不仅可以通过索引访问,还支持通过命名属性访问URL的各个部分.
"""

from urllib.parse import urlparse


url = 'http://user:pwd@NetLoc:80/path;para?query=arg#frag'
parsed = urlparse(url)

print(parsed)
print('scheme      : ', parsed.scheme)
print('netloc      : ', parsed.netloc)
print('path        : ', parsed.path)
print('params      : ', parsed.params)
print('query       : ', parsed.query)
print('fragment    : ', parsed.fragment)
print('username    : ', parsed.username)
print('password    : ', parsed.password)
print('hostname    : ', parsed.hostname)
print('port        : ', parsed.port)
