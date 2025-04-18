# -*- coding: utf-8 -*-

"""
python的控制流程
while && if条件中可以使用任意操作，不仅仅是比较操作
校验一个值是否在一个序列里：
    in,   not in
比较两个对象是否是同一个对象:
    is,   is not
比较操作可以传递, 如 a < b == c 校验a小于b并且b等于c
比较操作可以用and和or组合(任何布尔操作可以用not取反)
优先级not > 比较操作 > and > or
"""


def test_control() -> None:
    """
    if ... else ...
    """
    a = int(input("输入一个整数: "))
    
    if a % 2 == 0:
        print("输入的是偶数.")
    else:
        print("输入的是奇数.")



def test2_control() -> None:
    """
    if ... elif ... elif ... else ...
    """
    a = int(input("输入一个整数: "))

    if a < 0:
        print("输入的数小于0.")
    elif a == 0:
        print("输入的数等于0.")
    elif a > 0:
        print("输入的数大于0.")
    else:
        print("请输入整数.")


def test_loop() -> None:
    """
    test loop
    for
    while
    break
    continue
    """
    alist = [1, 2, 3, 4]
    for i in alist:
        if i % 2 == 0:
            print(i)
        else:
            continue    # break
    else:
        print("循环条件为假或迭代对象已循环耗尽.")

    for i in range(1, 5):   # 用于迭代一个有一定规律的整数序列
        print(i)    

    a = 0
    while not alist:
        alist.append(a)
        a = a + 1
        if len(alist) > 5:
            break
    print(alist)
    


if __name__ == "__main__":
    test_loop()