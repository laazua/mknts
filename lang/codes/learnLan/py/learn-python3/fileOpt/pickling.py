# -*- coding: utf-8 -*-

"""
序列化：将数据从内存变成可存储对象或传输对象的过程.
反序列化：把可存储对象或传输对象重新读写到内存中的过程.
"""

import pickle

def test_pickle():
    d = dict(a=1, b=2)
    res = pickle.dumps(d)
    print(res)


if __name__ == '__main__':
    test_pickle()