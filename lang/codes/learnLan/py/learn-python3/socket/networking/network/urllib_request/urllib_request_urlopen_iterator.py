# -*-coding:utf-8-*-
"""
urlopen()返回的类似文件对象是可以迭代的(iterable)
"""

from urllib import request


response = request.urlopen('http://localhost:8080/')
for line in response:
    print(line.decode('utf-8').rstrip())
