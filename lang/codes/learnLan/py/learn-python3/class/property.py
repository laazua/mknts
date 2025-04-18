# -*- coding: utf-8 -*-
"""
property装饰器负责把类的一个方法变成属性来调用,property包含3个方法的集合:getter, setter, deleter
"""


class Person:
    def __init__(self, name):
        self.name = name

    # getter方法
    @property
    def name(self):
        return self._name

    # setter方法
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('need a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('cant delete attribute!')


class SubPerson(Person):
    """扩展Person类name属性的功能"""
    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


a = Person("bb")
a.name = "cc"
print(a.name)

p = SubPerson("aa")
print(p.name)
