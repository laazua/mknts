# -*- coding:utf-8 -*-
"""
从打包的表示中解压数据
"""

import struct
import binascii


packed_data = binascii.unhexlify(b'1000000061620000cdcc2c40')

s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values: ', unpacked_data)
