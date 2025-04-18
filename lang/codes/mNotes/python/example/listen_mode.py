# -*- coding: utf -*-
"""
要明确谁是观察者谁是被观察者，只要明白谁是应该关注的对象，问题也就明白了。
一般观察者与被观察者之间是多对一的关系，一个被观察对象可以有多个监听对象（观察者）。

Observable 在发送广播通知的时候，无须指定具体的 Observer,Observer可以自己决定是否订阅Subject的通知

被观察者至少需要有三个方法：添加监听者、移除监听者、通知Observer的方法。观察者至少要有一个方法：更新方法，即更新当前的内容，做出相应的处理

添加监听者和移除监听者在不同的模型称谓中可能会有不同命名，如在观察者模型中一般是addObserver/removeObserver；
在源/监听器（Source/Listener）模型中一般是attach/detach，应用在桌面编程的窗口中还可能是attachWindow/detachWindow或Register/UnRegister。
不要被名称弄迷糊了，不管它们是什么名称，其实功能都是一样的，就是添加或删除观察者
"""
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self) -> None:
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def delObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    def __init__(self) -> None:
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature: " + str(self.__temperature) + "C")
        self.notifyObservers()


class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("Washing...")


class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("Drinking...")

    
def test_water_heater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


if __name__ == "__main__":
    test_water_heater()