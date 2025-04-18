# -*- coding: utf-8 -*-
"""
常见异常:
SyntaxError
TypeError
IndexError
KeyError
ValueError
AttributeError
NameError
IOError
StopIteration
AssertionError
IndentationError
ImportEror

异常捕获原则:
  -- 只捕获可能会抛出异常的语句，避免含糊的捕获逻辑
  -- 保持模块异常类的抽象一致性，必要时对底层异常类进行包装
  -- 使用上下文管理器可以简化重复的异常处理逻辑
"""
import os


def raise_error(file_name):
    if not os.path.isfile(file_name):
        raise("{}文件不存在!".format(file_name))


def try_except():
    """
    异常捕获
    """
    try:
        pass
    except [EXCEPTION]:
        pass

    try:
        pass
    except [EXCEPTION] as e:
        pass
        # raise SomeError("...") from None
        # raise SomeError("...") from e
        # raise SomeError("...").with_traceback(e)

    try:
        pass
    except [EXCEPTION] as e:
        pass
    else:
        print("如果发生异常,进入except代码逻辑块中,如果没有发生异常会走到else代码逻辑块中.")

    try:
        pass
    except [EXCEPTION] as e:
        pass
    finally:
        print("不管是否发生异常最后都要执行finally代码逻辑块.")

    try:
        pass
    except [EXCEPTION1] as e:
        pass
    except [EXCEPTION2] as e:
        pass
    except [EXCEPTION3] as e:
        pass


class InputError(Exception):
    """
    自定义异常
    """
    def __init__(self, mssage):
        self.message = mssage

    def __str__(self):
        return self.message
