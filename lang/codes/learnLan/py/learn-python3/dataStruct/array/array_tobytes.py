# -*- coding:utf-8 -*-
"""
tobytes() && frombytes()处理字节串,而不是Unicode字符串
"""
import array
import binascii


a = array.array('i', range(5))
print('a: ', a)

as_bytes = a.tobytes()
print('bytes: ', binascii.hexlify(as_bytes))

aa = array.array('i')
aa.frombytes(as_bytes)
print('aa: ', aa)
