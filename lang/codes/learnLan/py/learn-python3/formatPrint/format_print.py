# -*- coding: utf-8 -*-

"""
格式化输入输出
"""


def test_format() -> None:
    """
    test format print
    :return: None
    """
    year = 2020
    month = 10
    print(f'{year}-{month}')
    print('{:12}-{:2}'.format(year, month))

    aa = 3.14159
    print(f'{aa:.2f}')
    print('{:.2f}'.format(aa))

    print('%.3f' % aa)


if __name__ == "__main__":
    test_format()