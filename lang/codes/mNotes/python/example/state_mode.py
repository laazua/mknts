# -*- coding: utf-8 -*-

# 状态模式


from abc import ABCMeta, abstractmethod
from os import name, stat


class Water:
    def __init__(self, state) -> None:
        self.__temperature = 25
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if self.__state:
            print(self.__state.getName(), "change to", state.getName())
        else:
            print("init to: ", state.getName())
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.changeState(SolidState("SolidState"))
        if self.__temperature <= 100:
            self.changeState(LiquidState("LiquidState"))
        if self.__temperature > 100:
            self.changeState(GaseousState("GaseousState"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    def __init__(self, name) -> None:
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):
    def __init__(self, name) -> None:
        super().__init__(name)

    def behavior(self, water):
        print("SolidState current temperature: " + str(water.getTemperature()) + "C")

class LiquidState(State):
    def __init__(self, name) -> None:
        super().__init__(name)

    def behavior(self, water):
        print("LiquidState current temperature: " + str(water.getTemperature()) + "C")


class GaseousState(State):
    def __init__(self, name) -> None:
        super().__init__(name)

    def behavior(self, water):
        print("GaseousState current temperature: " + str(water.getTemperature()) + "C")


def test_state():
    water = Water(LiquidState("liquidState"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()

#######################################################

class Context(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0

    def addState(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("init state to: ", state.getName())
        else:
            print(self.__curState.getName(), "change to: ", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    def __init__(self, name) -> None:
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, statInfo):
        return False

    @abstractmethod
    def behavior(self, context):
        pass

class Wate(Context):
    def __init__(self) -> None:
        super().__init__()
        self.addState(SolidState("SolidState"))
        self.addState(LiquidState("LiquidState"))
        self.addState(GaseousState("GaseousState"))
        self.setTemperature(25)
    
    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton


@singleton
class SolidState(State):

    def __init__(self, name) -> None:
        super().__init__(name)

    def isMatch(self, statInfo):
        return statInfo <0

    def behavior(self, context):
        print("SolidState current state: ", context._getStateInfo(), "C")


@singleton
class LiquidState(State):
    def __init__(self, name) -> None:
        super().__init__(name)

    def isMatch(self, statInfo):
        return statInfo <= 100

    def behavior(self, context):
        print("LiquidState current state: ", context._getStateInfo(), "C")


@singleton
class GaseousState(State):
    def __init__(self, name) -> None:
        super().__init__(name)

    def isMatch(self, statInfo):
        return statInfo > 100

    def behavior(self, context):
        print("GaseousState current state: ", context._getStateInfo(), "C")


def test_state():
    water = Wate()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()


if __name__ == "__main__":
    test_state()