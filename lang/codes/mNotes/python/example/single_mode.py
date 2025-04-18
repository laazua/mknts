
"""单例模式"""

class SingleOne:
    """单例模式实现1"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            SingleOne.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            SingleOne.__isFirstInit = True

    def get_name(self):
        return self.__name


# test
ton = SingleOne("tony")
kar = SingleOne("kar")
print(ton.get_name(), kar.get_name())
print("id(ton): ", id(ton), "id(kar): ", id(kar))
print("ton == kar: ", ton is kar)


class SingleTow(type):
    """单例实现2"""
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwds):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwds)
        return cls._instance


class Custom(metaclass=SingleTow):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# test
ton = Custom("tony")
kar = Custom("kar")
print(ton.get_name(), kar.get_name())
print("id(ton): ", id(ton), "id(kar): ", id(kar))
print("ton == kar: ", ton is kar)


def SingleWrapper(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}
    def wrapperSingle(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingle


@SingleWrapper
class SingleThree:
    """使用单例装饰器修饰一个类"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# test
ton = SingleThree("tony")
kar = SingleThree("kar")
print(ton.get_name(), kar.get_name())
print("id(ton): ", id(ton), "id(kar): ", id(kar))
print("ton == kar: ", ton is kar)
