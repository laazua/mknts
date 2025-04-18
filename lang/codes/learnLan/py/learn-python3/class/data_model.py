# -*- coding: utf-8 -*_
"""
定义某些在属性赋值上面有限制的数据结构,使用描述器
"""


class Descriptor:
    """使用描述器实现一个系统类型和赋值验证框架"""

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """用描述器限制类型"""

    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """用描述器限制值"""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


# 以上就是要创建的数据模型或类型的记i处构建模块,以下就是实际定义的各种不同的数据类型
class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# 使用自定义数据类型
class Stock:
    # 具体约束
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# 使用装饰器来约束数据结构和值
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate


# 例子
@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, pric=UnsignedFloat)
class Stock1:
    def __int__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# 使用元类来约束数据结构和值
class CheckMeta(type):
    def __new__(mcs, *args, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(mcs, args, kwargs)


# 例子
class Stock2(metaclass=CheckMeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# 使用装饰器和元类可以简化代码
class Point:
    x = Integer('x')
    y = Integer('y')


class Point1(metaclass=CheckMeta):
    x = Integer()
    y = Integer()


# 所有方法中装饰器是最灵活和最高明的,并且执行速度很快
def typed(expected_ype, cls=None):
    """装饰器来检查"""
    if cls is None:
        return lambda cls: typed(expected_ype, cls)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_ype):
            raise TypeError('expected ' + str(expected_ype))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for allowing sized values
def max_sized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# specialized descriptors
@type(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass
