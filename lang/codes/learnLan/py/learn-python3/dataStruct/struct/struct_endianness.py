# -*- coding:utf-8 -*-
"""
默认地, 值会使用原生C库的字节序(endianness)来编码.只需要在格式串中提供一个显式的字节序指令, 就可以很容易地覆盖这个默认选择.
"""

import struct
import binascii


values = (1, 'ab'.encode('utf-8'), 2.7)
print('Original values: ', values)

# @ <==> 原生顺序; = <==> 原生标准; < <==> 小端; > <==> 大端; ! <==> 网络顺序
endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print()
    print('Format    string: ', s.format, 'for', name)
    print('Uses            : ', s.size, 'bytes')
    print('Packed     value: ', binascii.hexlify(packed_data))
    print('Unpacked   value: ', s.unpack(packed_data))
