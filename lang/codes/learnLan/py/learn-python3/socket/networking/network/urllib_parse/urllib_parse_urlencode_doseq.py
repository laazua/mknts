# -*-coding:utf-8 -*-
"""
调用urlencode()将doseq设置为True, 可以利用查询串中的变量传递一个序列值
"""

from urllib.parse import urlencode, parse_qs, parse_qsl


query_args = {
    'foo': ['foo1', 'foo2'],
}

print('Single        : ', urlencode(query_args))
print('Sequence      : ', urlencode(query_args, doseq=True))


# 解码上面的查询串, 可以使用parse_qs, parse_qsl
enncoded = 'foo=foo1&foo=foo2'
print('parse_qs    : ', parse_qs(enncoded))
print('parse_qsl   : ', parse_qsl(enncoded))
