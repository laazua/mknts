# -*-coding:utf-8-*-
"""
从请求提交表单数据
    建立Request时, 可以指定发送的数据, 从而将其提交给服务器
"""

from urllib import parse
from urllib import request


query_args = {'q': 'query_string', 'foo': 'bar'}
r = request.Request(
    url='http://localhost:8080/',
    data=parse.urlencode(query_args).encode('utf-8')
)
print('Request method : ', r.get_method())
r.add_header(
    'User-agent',
    'PyMOTW(https://pymotw.com/)',
)

print()
print('OUTGOING DATA:')
print(r.data)

print()
print('SERVER RESPONSE:')
print(request.urlopen(r).read().decode('utf-8'))
