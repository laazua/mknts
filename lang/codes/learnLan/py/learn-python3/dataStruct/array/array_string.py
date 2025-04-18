# -*-coding:utf-8 -*-
"""
array实例化一个对象并提供参数来描述允许哪种类型的数据
"""
import array
import binascii


s = 'hello world'
a = array.array('b', s)

print('As byte string: ', s)
print('As array      : ', a)
print('As hex         : ', binascii.hexlify(a))
