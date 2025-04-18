# -*- coding: utf-8 -*-

"""
类:用于包装数据和方法
类就像模板,实例是类具象出来的一个具体的对象
类中属性的封装,一单下划线_命名的属性表示为私有(该约定适用于模块和函数的封装);以双下划线__命名的属性在类继承过程中不会被覆盖.
"""


class Test1:
    """
    这是一个示例类
    """
    def __init__(self, data):
        """
        实例化一个对象时,做一些初始化工作
        """
        self.data = data
        self.index = len(data)

    def __iter__(self):
        """
        给类添加迭代器行为,配合__next__(self)方法
        """
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class Student:
    """
    __slots__ = ('x', 'y')，固定类变量,类属性只能添加x ,y
    @property装饰器负责把类方法变成一个属性
    """
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if not isinstance(val, int):
            raise ValueError("age must be integer!")
        if val < 0:
            raise ValueError("age must be greater 0!")
        self._age = val


if __name__ == "__main__":
    a = Test1([1,2,3])
    for i in a:
        print(i)

    print("==============")

    s = Student
    s.age = 20
    print(s.age)