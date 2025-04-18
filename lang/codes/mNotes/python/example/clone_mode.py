"""克隆模式"""
from copy import copy, deepcopy


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


ton = Person("ton", 18)
print(ton.get_name(), ton.get_age())

ton_one = ton.clone()
print(ton_one.get_name(), ton_one.get_age())