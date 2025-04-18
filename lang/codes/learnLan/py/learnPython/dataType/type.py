# -*- coding: utf-8 -*-
"""
type()：
  -- 判断对象类型的函数
  -- 动态创建类

  type --> 元类 --> 类 --> 实例
"""

class BaseClass:
    def speak(self):
        print("hahah")


def say(self):
    print("hello")


User = type("User", (BaseClass, ), {"name": "user", "say": say})


if __name__ == "__main__":
    type(int)
    type(type)
    type(object)

    u = User()
    u.say()