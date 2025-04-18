# -*- coding:utf-8 -*-
"""
通常在强调性能的情况下或者向扩展模块传入或传出数据时才会处理二进制打包数据, 通过避免为每个打包结构分配一个新缓冲区所带来的开销, 这些情况
可以得到优化. pack_into()和unpack_from()方法支持直接写入预分配的缓冲区.
"""

import array
import binascii
import ctypes
import struct


s = struct.Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)

print('Original values: ', values)
print()

print('ctypes string buffer')
b = ctypes.create_string_buffer(s.size)
print('Before    : ', binascii.hexlify(b.raw))
s.pack_into(b, 0, *values)
print('After     : ', binascii.hexlify(b.raw))
print('Unpacked  : ', s.unpack_from(b, 0))

print()
print('array')

a = array.array('b', b'\0' * s.size)
print('Before    : ', binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('After     : ', binascii.hexlify(a))
print('Unpacked  : ', s.unpack_from(a,  0))

# Struct的size属性指出缓冲区需要有多大
