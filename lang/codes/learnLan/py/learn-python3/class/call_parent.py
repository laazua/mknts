# -*- coding: utf-8 -*
"""
调用夫类的某个已经被覆盖的方法,  super()
"""


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam      # 调用父类同名方法
        # python2.x   super(B, self).spam()


o = B()
o.spam()
