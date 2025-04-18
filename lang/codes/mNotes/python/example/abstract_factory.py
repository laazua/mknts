# -*- coding:utf-8 -*-
# 抽象工厂模式

class CarBody:
    def __init__(self):
        pass


class CarWhell:
    def __init__(self):
        pass


class TruckBody:
    def __init__(self):
        pass


class TrucWheel:
    def __init__(self):
        pass

class CarFactory:
    """实现car的工厂类"""
    def create_body(self):
        return CarBody()
    
    def create_wheel(self):
        return CarWhell()


class TruckFactory:
    """实现truck的工厂类"""
    def create_body(self):
        return TruckBody()

    def create_wheel(self):
        return TrucWheel()


class Assemble:
    """组装车子类"""
    def __init__(self, t):
        self.type = t
        self.body = None
        self.wheel = None

    def set_body(self, b):
        self.body = b

    def set_wheel(self, w):
        self.wheel = w

    def print(self):
        print("===", self.type, "===")
        print(type(self.body))
        print(type(self.wheel))


def make(type, factory, wheel):
    a = Assemble(type)
    a.set_body(factory.create_body())
    a.set_wheel(factory.create_wheel())

    return a


if __name__ == '__main__':
    make('Car', CarFactory(), 4).print()
    make('Truck', TruckFactory(), 6).print()