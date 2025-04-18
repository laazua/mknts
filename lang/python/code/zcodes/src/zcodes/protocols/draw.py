"""
协议接口
"""
from typing import Protocol


class Drawable(Protocol):
    """绘画协议"""
    def draw(self) -> None:
        ...
