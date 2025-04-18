# -*-coding:utf-8 -*-
"""
HTTP GET操作是urllib.request最简单的用法. 通过将URL传递到urlopen()来得到远程数据的一个'类似文件'的句柄
"""

from urllib import request


response = request.urlopen('http://localhost:8080/')
print('RESPONSE   : ', response)
print('URL        : ', response.geturl())

headers = response.info()
print('DATE       : ', headers['date'])
print('HEADERS    :')
print('------------')
print(headers)

data = response.read().decode('utf-8')          # readlines()也可以访问远程资源的相应数据
print('LENGTH     : ', len(data))
print('DATA       : ')
print('data')
