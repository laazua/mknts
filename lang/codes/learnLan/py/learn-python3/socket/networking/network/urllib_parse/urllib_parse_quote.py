# -*-coding:utf-8 -*-
"""
查询参数中可能有一些特殊字符, 会导致服务端在解析URL时出现问题,所以在传递到urlencode()时要对这些特殊字符"加引号", 要在本地对他们加引号
以建立这些串的安全版本,可以直接使用quote()或quote_plus()函数
"""

from urllib.parse import quote, quote_plus, urlencode, unquote, unquote_plus


url = 'http://localhost:8080/~hellmann/'
print('urlencode()        : ', urlencode({'url': url}))
print('quote()            : ', quote(url))
print('quote_plus()       : ', quote_plus(url))


# 要完成加引号操作的逆过程, 可以在适当的时候使用unquote()或unquote_plus()
print(unquote('http%3A//localhost%3A8080/~hellmann/'))
print(unquote_plus('http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F'))
