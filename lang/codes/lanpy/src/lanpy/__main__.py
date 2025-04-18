"""
entry point
"""
import os

from lanpy.impl import Person
from lanpy.impl import Animal
from lanpy.impl import Bmw
from lanpy.impl import Benz
from lanpy.service import who
from lanpy.service import drive
from lanpy.config import load_env


def main():
    # 加载配置
    load_env(".env")
    print(os.getenv("app.name"))

    p = Person("zhang san")
    a = Animal("xiao mao mi")

    who(p)
    who(a)

    bmw = Bmw("bmw")
    benz = Benz("Benz")

    drive(bmw)
    drive(benz)


if __name__ == '__main__':
    main()
