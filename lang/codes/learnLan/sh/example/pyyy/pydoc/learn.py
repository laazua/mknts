#!/usr/bin/python3
#coding:utf-8

print(
    """
    运算符:
        + - * / **  ^
        == != > < >= <=
        and or not
        in
        
    值和类型:
        type(object)
        str, number, list, dict, tuple, set
        
    变量:
        字母数字或者下划线,但是字母不能在开头命名
    
    表达式:
        数值,变量和运算符的组合
        
    函数:
        一系列语句的组合.
        
    控制结构:
        if condition:
            statement
        elif condition:
            ...
        else:
            statement
            
        while condition:
            statement
            
        for num in [1, 2, 3]:
            statement
        for num in range(1, 4):
            statement
            
    模块:
        pickle 将类型对象转换为字符串
        ...
        
    类 && 对象:
        属性
        方法
    """
)

print(
    """
        *args  **kwargs
        
        可迭代对象(Iterable)
            python中任意的对象,只要它定义了一个迭代器的__iter__方法,或者定义了一个可以支持下表索引的__getitem__方法,那么它就是一个
            可迭代对象.
        迭代器(Iterator)
            任意对象,只要定义了next或者__next__方法,那么它就是一个迭代器.
        迭代(Iteration)
            迭代就是从某个地方(比如列表)取出一个元素的过程.
        生成器(Generators)
            生成器也是一种迭代器,但是只能对其迭代一次.这是因为它们并没有把值存在内存中,而是在运行时生成值.大多时候生成器是以函数来实现
            的.但是它们并不返回一个值,而是yield一个值.(应用场景:不想同一时间将所有计算出来的结果分配到内存中,特别是结果中包含循环.)
    """
)