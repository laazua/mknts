# -*- coding: utf-8 -*-

"""
内存中二进制操作
"""

from io import BytesIO

def test_bytes():
    fd = BytesIO()
    r = fd.write("测试".encode('utf-8'))
    print(fd.getvalue())

    f = BytesIO(b'\xe4/xb9\xb3')
    print(f.read())


if __name__ == '__main__':
    test_bytes()