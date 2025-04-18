# -*- coding:utf-8 -*-
"""
python魔法知识
"""

# python3中的...在python2为Ellipsis
type(...)    # <class 'ellipsis'>
bool(...)    # True

# ...是Numpy的一个语法糖
# 在python3中...可以代替pass

def foo():
    pass

# python3中可以这样写
# def foo():
#     ...


# 使用end来结束代码块
__builtins__.end = None

def bar(x):
    if x > 0:
        return x
    else:
        return -x
    end
end


# 可以直接运行的zip包
"""
[root@localhost ~]# ls -l demo
total 8
-rw-r--r-- 1 root root 30 May  8 19:27 calc.py
-rw-r--r-- 1 root root 35 May  8 19:33 __main__.py
[root@localhost ~]#
[root@localhost ~]# cat demo/__main__.py
import calc

print(calc.add(2, 3))
[root@localhost ~]#
[root@localhost ~]# cat demo/calc.py
def add(x, y):
    return x+y
[root@localhost ~]#
[root@localhost ~]# python -m zipfile -c demo.zip demo/*
[root@localhost ~]#
"""

# 链式比较
# False == False == True    等价    False == False and False == True


# or与and
# 当一个or表达式中所有的值都为真,python会选择第一个值
# 当一个and表达式中所有值都为真,python会选择最后一个值
# >>> (2 or 3) * (5 and 6 and 7)
# 上面的结果是 2 * 7


# 连接多个列表最极客的方式
# >>> a = [1, 2]
# >>> b = [3, 4]
# >>> c = [5, 6]
# >>> sum((a, b, c), [])
# [1, 2, 3, 4, 5, 6]


# 离线学习python模块 python -m pydoc -p 9999

# 优雅的安装python包
# python -m pip install package      这里的python是默认的python解释器
# python3.7 -m pip install package


# 连接列表的方式
# 方式1: list1 + list2
# 方式2: itertools包
# 方式3: [*list1, *list2]
# 方式4: list1.extend(list2)
# 方式5: [x for l in (list1, list2) for x in l]
# 方式6: from heapq import merge; list(merge(list1, list2))    合并后的列表有序
# 方式7: list1.__add__(list2)    借助魔法方法, reduce(list.__add__, (list1, list2, list3))
# 方式8: def merge(*lists):
#            for l in lists:
#                 yield from l
#        list(merge(list1, list2, list3))


# 合并字典的方式
# 方式1: dict1.update(dict2)    原地更新
# 方式2: from copy import deepcopy; dict1 = deepcopy(dict2); dict1.update(dict3) 生成字典dict1后再更新
# 方式3: dict1 = {**dict2, **dict3} 或者 dict1 = dict(**dict2, **dict3)
# 方式4: import itertools; dict(itertools.chain(dict1.items(), dict2.items()))
# 方式5: import collections; dict(collections.ChainMap(dict1, dict2)) 当字典中存在重复键时,取第一个键
# 方式6: dict(dict1.items() | dict2.items())
# 方式7: dict(list(dict1.items()) + list(dict2.items()))
# 方式8: {k:v for d in [dict1, dict2] for k, v in d.items()}
# 方式9: dict1 | dict2   python3.9   或者 dict1 |= dict2  原地更新


# 导入包的方法
# 方式1: import package
# 方式2: __import__函数,  os = __import__('os')
# 方式3: os = __builtins__.__dict__['__import__']('os')
# 方式4: import importlib; os = importlibs.import_module('os')
# 方式5: import imp; file, pathname, desc = imp.find_module('os'); os = imp.load_module('sep', file, pathname, desc)
# 方式6: python3 -m pip install import_from_github_com; from github_com.zzzeek import sqlalchemy

# 条件语句的七种写法
age = 20
# 方式1:
if age > 2:
    print(age)
else:
    print(-age)
# 方式2:
# <on_true> if <condition> else <on_false>
print(age) if age > 18 else print(-age)

# 方式3:
# <condition> and <on_true> or <on_false>
age = 20 > 18 and age or -age

# 方式4:
#(<on_false>, <on_true>)[condition]
age = (age, -age)[2 > 1]

# 方式5:
# (lambda: <on_false>, lambda: <on_true>)[<condition>]()
msg = (lambda: 'a', lambda: 'b')[age > 18]()

#方式6:
# {True: <on_true>, False: <on_false>}[<condition>]
msg = {True: 'a', False: 'B'}[age > 18]

#方式7:
# ((<condition>) and (<on_true>, ) or (<on_false>,))[0]
msg = ((age > 18) and ('a',) or ('b',))[0]

# 海象运算 :=  python3.9
# if/else
if (age := 20) > 18:
    print('已经成年')

# while
fd = open('test.txt', 'r')
while(line := fd.readline()):
    print(line.strip())

while (p := input('please input: ')) != 'checkinput':
    continue


# 模块重载
# python2 reload(moduleName)
# python3.0-3.3 imp.reload(moduleName)
# python3.4+ importlib.reload(moduleName)
# moduleName.__spec__.loader.load_module()
# import sys; del sys.modules['paclage.moduleName']; import package.moduleName


# 读取文件的三种方式
with open('test.txt') as fd:
    print(fd.readline())

import fileinput
with fileinput.input(files=('data,txt',)) as fd:
    print([line for line in fd])

import linecache
print(linecache.getlines('data.txt'))


# 优雅读取超大文件(read()指定字节)
def read_from_file(filename, block_zize = 1024 * 8):
    with open(filename, 'r') as fd:
        while True:
            chunk = fd.read(block_zize)
            if not chunk:
                break
            yield chunk

# 优雅写法
from functools import partial
def read_big_file(filename, block_size = 1024 * 8):
    with open(filename, 'r') as fd:
        for chunk in iter(partial(fd.read, block_size), ""):
            yield chunk

