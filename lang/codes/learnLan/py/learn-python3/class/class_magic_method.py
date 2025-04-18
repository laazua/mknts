# -*- coding: utf-8 -*-
"""
魔术方法是面向对象的python的一切,它们总是被双下划线包围着

__new__(cls, [...]):
    实例化对象时调用的第一个方法, 它的第一个参数是这个类本身. 其他参数是用来直接传递给__init__方法

__init__(self, [...]): 
    此方法可以给定义的对象做一些初始化操作.

__del__(self):
    __new__和__init__是对象的构造器的话, 那么__del__就是析构器;它定义的是一个对象进行垃圾回收时候的行为;当对象在删除的时候,
    需要更多的清洁工作的时候此方法会很有用, 比如套接字或者是文件对象


用于比较的魔术方法:
__eq__(self, other): 定义了等号的行为, ==
__ne__(self, other): 定义了不等号的行为, !=
__lt__(self, other): 定义了小于号的行为, <
__gt__(self, other): 定义了大于号的行为, >


数值处理的魔术方法:
__pos__(self): 实现正号的特性
__neg__(self): 实现负号的特性
__abs__(self): 实现内置abs()函数的特性
__invert__(self): 实现 ~ 符号的特性


普通算数操作符的魔术方法:
__add__(self, other): 加法
__sub__(self, other): 减法
__mul__(self, other): 乘法
__floordiv__(self, other): //符号
__div__(self, other): 除法
__truediv__(self, other): 真除法    # from __future__ import division 才起作用
__mod__(self, other): 取模算法
__divmod__(self, other): 实现内置divmod()算法
__pow__(self, other): 指数运算**
__lshift__(self, other): <<左移运算
__rshift__(self, other): >>右移运算
__and__(self, other): 按位 &
__or__(self, other): 按位 |
__xor__(self, other): 按位异或 ^


反运算
__radd__(self, othor): 实现反加
__rsub__(self, other): 反减法
__rmul__(self, other): 反乘法
__rfloordiv__(self, other): 反//符号
__rdiv__(self, other): 反除法
__rtruediv__(self, other): 反真除法    # from __future__ import division 才起作用
__rmod__(self, other): 反取模算法
__rdivmod__(self, other): 实现反内置divmod()算法
__rpow__(self, other): 反指数运算**
__rlshift__(self, other): 反<<左移运算
__rrshift__(self, other): 反>>右移运算
__rand__(self, other): 反按位 &
__ror__(self, other): 反按位 |
__rxor__(self, other): 反按位异或 ^


增量赋值
__iadd__(self, other): +=
__isub__(self, other): -=
__imul__(self, other): *=
__ifloordiv__(self, other): //=
__idiv__(self, other): /=
__itruediv__(self, other): 赋值真除法    # from __future__ import division 才起作用
__imod__(self, other): %=
__ipow__(self, other): 指数运算**=
__ilshift__(self, other): <<=左移运算
__irshift__(self, other): >>=右移运算
__iand__(self, other): 按位 &=
__ior__(self, other): 按位 |=
__ixor__(self, other): 按位异或 ^=


类型转换
__int__(self): 整型强制转换
__long__(self): 长整型强制转换
__float__(self): 浮点型强制转换
__complex__(self): 复数强制转换
__oct__(self): 八进制强制转换
__hex__(self): 二进制强制转换
__index__(self): 当对象是被应用在切片表达式中时,实现整型强制转换
__trunc__(self): 当使用math.trunc(self)的时候被调用.
__coerce__(self, other): 实现混合模式算数,转换失败返回None

表现类
__str__(self): 人类可读
__repr__(self): 机器可读
__unicode__(self): 返回unicode字符串
__hash__(self): hash调用时候的返回值
__nonzero__(self): 调用 时返回bool值


控制属性访问
__getattr__(self, name)
    当获取一些不存在的属性或不建议的属AttributeError,这不是一个封装的解决方案
__setattr__(self, name, value)
    无论属性是否存在,都可以定义属性的赋值行为; 注意防止无限递归
__delattr__(self, name)
    与上面一个方法相同删除一个属性,防止递归调用


容器魔法
__len__(self): 容器长度
__getitem__(self, key): 定义一个条目被访问,使用符号self[key], 如果键的类型错误或者KeyError或者没有适合的值,抛出TypeError
__setitem__(self, key, value): 定义一个条目被赋值时的行为,使用self[key] = value
__delitem__(self, key): 定义一个条目被删除时的行为,使用del self[key], 当使用一个无效的键时应该抛出适当异常
__iter__(self): 返回一个可迭代的容器
__reversed__(self): 实现当revesed()被调用时的行为
__contains__(self, item): 当调用in或者not in来测试成员是否存在时,__contains__被定义.
__concat__(self): 定义连接两个序列的时候的行为


反射
__instancecheck__(self, instance): 检查一个实例是否是定义的类实例
__subclasscheck__(self, subclass): 检查一个类是否是定义的类的子类


可调用对象
__call__(self, [args...]): 可以让类的实例的行为表现得像函数一样,你可以调用它们,将一个函数当作参数传递到另外一个函数中


上下文管理(with语句)
__enter__(self):
__exit__(self, exception_type, exception_value, traceback)


创建对象描述器(至少有__get__或者__set__并且__delete__被实现)
__get__(self, instance, owner): 定义描述器的值被取得的时候的行为(instance是拥有者对象的一个实例, owner是拥有者类本身)
__set__(self, instance, value): 定义描述器值被改变时候的行为(instance是拥有者类的一个实例, value是要设置的值)
__delete__(self, instance): 定义描述器的值被删除的行为.


存储对象
__getstate__(self)
__setstate__(self)


=====================================================================================================

魔术方法                        调用方式                            解释
__new__(cls [,...])             instance = MyClass(arg1, arg2)      __new__ 在创建实例的时候被调用
__init__(self [,...])           instance = MyClass(arg1, arg2)      __init__ 在创建实例的时候被调用
__cmp__(self, other)            self == other, self > other, 等     在比较的时候调用
__pos__(self)                   +self                               一元加运算符
__neg__(self)                   -self                               一元减运算符
__invert__(self)                ~self                               取反运算符
__index__(self)                 x[self]                             对象被作为索引使用的时候
__nonzero__(self)               bool(self)                          对象的布尔值
__getattr__(self, name)         self.name # name不存在              访问一个不存在的属性时
__setattr__(self, name, val)    self.name = val                     对一个属性赋值时
__delattr__(self, name)         del self.name                       删除一个属性时
__getattribute(self, name)      self.name                           访问任何属性时
__getitem__(self, key)          self[key]                           使用索引访问元素时
__setitem__(self, key, val)     self[key] = val                     对某个索引值赋值时
__delitem__(self, key)          del self[key]                       删除某个索引值时
__iter__(self)                  for x in self                       迭代时
__contains__(self, value)       value in self, value not in self    使用 in 操作测试关系时
__concat__(self, value)         self + other                        连接两个对象时
__call__(self [,...])           self(args)                          "调用"对象时
__enter__(self)                 with self as x:                     with 语句环境管理
__exit__(self, exc, val, trace) with self as x:                     with 语句环境管理
__getstate__(self)              pickle.dump(pkl_file, self)         序列化
__setstate__(self)              data = pickle.load(pkl_file)        序列化
"""

