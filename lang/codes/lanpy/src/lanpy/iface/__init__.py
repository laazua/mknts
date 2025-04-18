"""
所有接口类放在此包下
"""

from abc import ABC, abstractmethod


class ICar(ABC):
    """
    定义一些抽象方法，要求继承此接口类必须实现这些抽象方法
    """
    @abstractmethod
    def drive(self):
        pass