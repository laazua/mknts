"""
所有协议类模块放在此包下
"""
from typing import Protocol


class Species(Protocol):
    """
    协议类不要求所有子类强制实现特定的方法
    """
    def sing(self):
        ...

    def running(self):
        ...
