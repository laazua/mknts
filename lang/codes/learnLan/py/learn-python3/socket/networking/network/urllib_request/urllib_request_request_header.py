# -*-coding-8-
"""
urlopen()是 一个便利函数, 隐藏了一些处理请求的细节. 可以使用Request实例提供更精确的控制
"""

from urllib import request

r = request.Request('http://localhost:8080/')
r.add_header(
    'User-agent',
    'PyMOTW(https://pymotw.com/)',
)

response = request.urlopen(r)
data = response.read().decode('utf-8')
print(data)
