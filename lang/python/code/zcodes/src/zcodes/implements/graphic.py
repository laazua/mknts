"""
实现 protocols下的协议接口
"""
from zcodes.protocols.draw import Drawable


class Circle(Drawable):
    def draw(self) -> None:
        print("Circle draw")


class Square(Drawable):
    def draw(self) -> None:
        print("Square draw")