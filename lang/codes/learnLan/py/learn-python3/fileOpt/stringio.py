# -*- coding: utf-8 -*-

"""
在内存中读写string
"""
from io import StringIO

def test_rwString():
    fd = StringIO()
    fd.write('hahaha')

    print(fd.getvalue())

    f = StringIO("dakeh;lehk;larje;rk")
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


if __name__ == '__main__':
    test_rwString()