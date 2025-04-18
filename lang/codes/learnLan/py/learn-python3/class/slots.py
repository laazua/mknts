# -*- coding: utf-8 -*-
"""
当创建大量对象时,通过给类添加slots可以极大的减少实例所占内存,但是拥有slots的类不会支持一些类的普通特性,比如多继承等,因为添加了slots的类
所创建的实例,其内部的数据都被固定到一个固定大小的数组里,而不是为每个实例定义一个字典
"""


class Test:
    """_slots test"""
    __slots__ = ["name", "age", "grade"]

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


t = Test("xiao ming", 12, "five")


print(t.name)