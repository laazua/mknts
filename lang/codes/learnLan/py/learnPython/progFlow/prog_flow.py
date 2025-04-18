# -*- coding: utf-8 -*-
"""
程序控制
"""

def if_test(a: int):
    if a < 0:
        print("a小于0")
    elif a > 0:
        print("a大于0")
    else:
        print("a等于0")

    """
    if object:
        print('ok')

    if not object:
        print('not ok')

    if object_1 and object_2:
        print('...')

    if object_1 or object_2:
        print('...')
    """


def for_test(a: list):
    for i in a:
        print(i)
    
    """
    break中断循环, continue跳过当前循环进入下一个循环
    for i in a:
        if i == i:
            continue
        print(i)
    else:
        print('循环正常执行完毕后,执行此代码, 否则不执行此代码')
        # 如果上面的continue换成break,这里的代码就不会执行

    l = [i for i in range(10)]
    """
    

def while_test(a: int):
    while a < 10:
        print(a)
        a += 1

    """
    while True:
        pass

    while condition:
        pass
    else:
        print('while循环正常执行完毕,执行此代码')
    """

if __name__ == "__main__":
    # if_test(5)
    # for_test([1,2])
    # while_test(5)

    