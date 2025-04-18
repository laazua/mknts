# -*- coding:utf-8 -*-
"""
urlparse(), 可以由相对片段构造绝对URL
"""
from urllib.parse import urljoin

print(urljoin('http://www.example.com/path/file.html', 'anotherfile.html'))
print(urljoin('http://www.example.com/path/file.html', '../anotherfile.html'))


print(urljoin('http://www.example.com/path/', '/subpath/file.html'))
print(urljoin('http://www.example.com/path/', 'subpath/file.html'))
