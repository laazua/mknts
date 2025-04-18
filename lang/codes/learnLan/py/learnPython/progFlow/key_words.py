# -*- coding: utf-8 -*-
"""
python关键字:
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

console模式下
help(): help(模块名), 模块要先导入.
dir(): 返回指定对象的属性列表, 不传入对象则返回当前作用域的名称.

type(): 确定对象类型.
hasattr(): 确定对象是否包含某个属性.
getattr(): 获取对象属性值.
id(): 返回对象的标识.
isinstance(): 确定对象是否是某个特定类型.
callable(): 确定对象是否可调用.

模块属性:
__doc__: 查询模块文档.
__name__: 始终是定义时的模块名,即使导入时给模块取别名, import json as js; js.__name__ # 'json'.
__file__: 模块的文件路径.
__dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象.

类：
__doc__: 类的文档字符串.
__name__: 始终是定义时的类名.
__dict__: 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象.
__module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象.
__bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类.

"""

def jumping_range(N):
    """
    jump = yield index语句
    - yield index 是将index return给外部调用程序
    - jump = yield 可以接收外部程序通过send()发送的信息,并赋值给jump
    """
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    itr = jumping_range(5)
    print(next(itr))
    print(itr.send(2))
    print(next(itr))
    print(itr.send(-1))