# -*- coding:utf-8 -*-
"""
urlsplit()函数可以替换urlparse(), 但行为稍有不同,因为他不会从URL分解参数 ,这对于遵循RFC 2396的url很有用
"""

from urllib.parse import urlsplit


url = 'http://user:pwd@NetLoc:80/p1;para/p2;para?query=arg#frag'
parsed = urlsplit(url)

print(parsed)
print('scheme      : ', parsed.scheme)
print('netloc      : ', parsed.netloc)
print('path        : ', parsed.path)
print('query       : ', parsed.query)
print('fragment    : ', parsed.fragment)
print('username    : ', parsed.username)
print('password    : ', parsed.password)
print('hostname    : ', parsed.hostname)
print('port        : ', parsed.port)