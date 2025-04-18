# -*- coding: utf-8 -*-
"""
上下文管理器
"""

class TestManager:
    """
    上下文管理器要实现__enter__(self)和__exit__(self)方法
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


import contextlib


@contextlib.contextmanager
def open_resource(file_name, model="r"):
    """
    yield之前的代码类似__enter__方法
    yield之后的代码类似__exit__方法
    """
    try:
        fd = open(file_name, model)
        yield fd
    except:
        print("打开文件失败!")
        fd.close()


if __name__ == "__main__":
    with open_resource("test.txt") as fd:
        pass
