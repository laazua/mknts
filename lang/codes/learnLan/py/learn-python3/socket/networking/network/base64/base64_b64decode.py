# -*-coding:utf-8-*-
"""
b64decode()将编码的串转换回原来的形式,它取4个字节, 利用一个查找表将这4个字节转换回原来的3个字节
"""

import base64

encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='

decoded_data = base64.b64encode(encoded_data)
print('Encoded : ', encoded_data)
print('Decoded : ', decoded_data)