# -*- coding:utf-8 -*-
"""
python装饰器库
https://wiki.python.org/moin/PythonDecoratorLibrary
"""
import time

def say_hello(name):
    '''
    被装饰的函数
    '''
    print("hello ", name)


def decorator(func):
    '''
    装饰器函数
    '''
    def wrapper(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)
    return wrapper


f = decorator(say_hello)
f('xiao ming')

print('-----------')


# 语法糖形式
@decorator
def say_hi(name):
    '''
    被装饰的函数
    '''
    print('hi ', name)


say_hi('xiao hong')