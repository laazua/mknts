# -*- coding: utf-8 -*-
"""
python基础数据类型,先创建再使用.
了解基本数据类型的一些常用方法的使用.
"""

def main():
    ## 字符串
    str_1 = "hello"
    str_2 = 'hello'
    str_3 = """hello"""
    str_4 = '''hello'''
    print(str_1 == str_2 == str_3 == str_4) # True

    ## 数字
    # 整数(int)
    a = 100
    # 浮点(float)
    b = 3.14
    print(a, b)

    # 复数
    c = 1 + 2j  # <class 'complex'>
    d = complex(1, 2)  # <class 'complex'>
    print(c , d)

    ## 布尔
    is_ok = True  # not is_ok == False
    print(is_ok, not is_ok)

    ## None

if __name__ == "__main__":
    main()