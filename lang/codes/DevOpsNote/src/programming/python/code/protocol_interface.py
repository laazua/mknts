from typing import Protocol


class MyProtocol(Protocol):
    def my_method(self) -> None:
        pass


class MyClass:
    def my_method(self) -> None:
        print("Implemented method")


def process(obj: MyProtocol) -> None:
    obj.my_method()


obj = MyClass()
process(obj)  # 输出: Implemented method
