# -*- coding:utf-8 -*-
"""
insort()函数是insort_right()函数的别名在原值的后面插入新值,insort_left()在原值的前面插入新值.
"""

import bisect


# a series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]


print('New Pos Contents')
print('---  ---  ------')
# use bisect_left and insort_left
l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)
    