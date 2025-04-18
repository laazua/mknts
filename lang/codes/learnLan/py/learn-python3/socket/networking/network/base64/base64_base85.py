# -*-coding:utf-8-*-
"""
Base85函数使用一个扩展的字母表,与Base64编码使用的字母表相比,在空间上更节省.
"""

import base64


original_data = b'this is the data, in the clear.'
print('Original  : {} bytes {!r}'.format(len(original_data), original_data))

b64_data = base64.b64encode(original_data)
print('b64 Encoded : {} bytes {!r}'.format(len(b64_data), b64_data))

b85_data = base64.b85encode(original_data)
print('b85 Encoded : {} bytes {!r}'.format(len(b85_data), b85_data))

a85_data = base64.a85encode(original_data)
print('a85 Encoded : {} bytes {!r}'.format(len(a85_data), a85_data))
