
# -*-coding:utf-8 -*-
"""
urllib.parse模块提供了一些函数,可以管理URL及其组成部分,包括将URL分解为组成部分以及由组成部分构成URL
urlparse()函数的返回值是一个ParseResult对象,相当于一个包含6个元素的tuple
"""

from urllib.parse import urlparse


url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed)

# ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')
