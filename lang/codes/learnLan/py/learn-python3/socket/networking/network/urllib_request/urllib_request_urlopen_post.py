# -*-coding:utf-8-
"""
使用POST而不是GET向远程服务器发送表单编码数据,可以把编码的查询参数作为数据传递到urlopen()
"""

from urllib import request
from urllib import parse


query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args).encode('utf-8')
url = 'http://localhost:8080/'
print(request.urlopen(url, encoded_args).read().decode('utf-8'))
