# -*- coding:utf-8 -*-

time = 0


def study_time(time):
    '''
    内部函数insert_time对变量time的修改不会影响全局作用域中的time值.
    '''
    def insert_time(min):
        '''
        内部函数的局部作用域可以访问外部函数局部作用域中的变量行为称之为闭包.
        '''
        nonlocal time
        time += min
        return time

    return insert_time



f = study_time(time)

print(f(8))