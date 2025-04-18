#_-*-coding:utf-8 -*-
"""
利用一些方法把分解的URL的各个部分重新组装在一起,形成一个串. 解析的URL对象有一个geturl()方法
geturl()方法只适用于urlparse()或urlsplit()返回的对象.
"""

from urllib.parse import urlparse

original = 'http://netloc/path;parrram?query=arg#frag'

print('ORIG      : ', original)

parsed = urlparse(original)
print('PARSED:   : ', parsed.geturl())
