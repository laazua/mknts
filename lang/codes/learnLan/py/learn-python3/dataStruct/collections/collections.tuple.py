# -*- coding:utf-8 -*-
"""
namedtuple在内存中使用很高效,且不可修改;各个属性名字不能冲突.
创建: namedtuple(className, strOfElement)
"""
import collections


Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=15)
print('Bob: ', bob)
print(bob.name, bob.age)

jane = Person(name='Jane', age=18)
print('Jane: ', jane)
print(jane.name, jane.age)



