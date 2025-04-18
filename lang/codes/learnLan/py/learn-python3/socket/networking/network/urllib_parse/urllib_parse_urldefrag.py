# -*-coding:utf-8 -*-
"""
从一个URL剥离出片段标识符, 如从一个URL查找基页面名, 可以使用urldefrag()
"""

from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('original: ', original)
d = urldefrag(original)

print('url     : ', d.url)
print('fragment: ', d.fragment)
