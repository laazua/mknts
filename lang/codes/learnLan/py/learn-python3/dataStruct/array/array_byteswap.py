# -*- coding:utf-8 -*-
"""
如果数组中的数据没有采用原生的字节顺序,或者在发送到一个采用不同字节顺序的系统(或在网络上发送)之前数据需要交换顺序,那么可以由python转换
整个数组而不必迭代处理每一个元素.
"""
import array
import binascii


def to_hex(a):
    chars_per_item = a.itemsize * 2    # 2 hex digits
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version) // chars_per_item
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]


start = int('0x12345678', 16)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt = '{:>12} {:>12} {:>12} {:>12}'
print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12))

fmt = '{!r:>12} {:12} {!r:>12} {:12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))
