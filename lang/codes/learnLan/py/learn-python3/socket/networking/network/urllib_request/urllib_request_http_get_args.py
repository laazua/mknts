# -*-coding:utf-8-*-
"""
可以利用urllib.parse.urlencode()对参数编码,并追加到URL, 从而将参数传递到服务器.
"""

from urllib import parse
from urllib import request


query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args)
print('Encoded    : ', encoded_args)

url = 'http://localhost:8080/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))
