"""
代码入口
"""
from services.render import render
from implements.graphic import Circle
from implements.graphic import Square

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    circle = Circle()
    square = Square()
    render(circle)
    render(square)