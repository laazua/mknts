"""
所有逻辑层模块放在此包下
"""
import functools
from typing import Callable

from lanpy.iface import ICar
from lanpy.proto import Species


def decorator(func: Callable) -> Callable:
    """
    不带参数的函数装饰器
    :param func: 被装饰的函数
    :return: wrapper
    """
    @functools.wraps(func)  # 保留被装饰函数的元信息: __name__, __doc__ 等
    def wrapper(*args, **kwargs):
        """
        :param args: 被装饰函数的位置参数
        :param kwargs: 被装饰函数的关键字参数
        :return:
        """
        print(f"species: {args[0]} ...")
        func(*args, **kwargs)
    return wrapper


@decorator
def who(species: Species):
    species.sing()
    species.running()


def drive(car: ICar):
    car.drive()