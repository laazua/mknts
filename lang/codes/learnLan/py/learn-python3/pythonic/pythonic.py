# -*- coding: utf-8 -*-

"""
pythonic代码
"""

# 交换变量值
x = 1
y = 2
x, y = y, x


# 连续赋值
a = b = c = 100


# 列表推导
mlist = []
for i in range(5):
    mlist.append(i)

mlist = [i for i in range(5)]

# 生成器表达式
ge = (x*2 for x in range(10))

# 字典推导
m = {x: x**2 for x in range(5)}

# 判断key是否在字典中
d = {1, "a"}
# 1 in d
d.get(1)

# 字典子集
def sub_dicts(d, keys):
    return {k: v for k, v in d.items() if  k in keys}
sub_dicts({1: "a", 2: "b", 3: "c"}, [1, 2])

# 反转字典
d = {1: "a", 2: "b", 3: "c", 4: "d"}
d = zip(d.values(), d.keys())
dict(z)


# 集合推导
nums = {n**2 for n in range(10)}

# 索引遍历
for i in range(len(mlist)):
    print(i, mlist[i])

for i, item in enumerate(mlist):
    print(i, item)


# 序列解包
a, *last = ["a", "b", "c", "d", "e", "f", "g"]

a, *middle, c = ["a", "b", "c", "d", "e", "f", "g"]


# 字符串拼接
mlist = ["a", "b", "c", "d", "e", "f", "g"]
result = ""
for s in mlist:
    result += s

word = ''.join(mlist)


# "",[],{}等条件判断
a = []
if a:
    print("Null")


# 访问字典元素
test = {1: "a", 2: "b", 3: "c"}
if test.keys == 1:
    print("a")
else:
    print("key == 1 not in.")

print(test.get(1, "key == 1 not in."))


# 过滤列表中的元素
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []
for i in a:
    if i > 3:
        b.append(i)

b = []
b = [i for i in a if i > 3]
# or
b = filter(lambda x: x > 3, a) # b = map(lambda x: x + 2, a)


# 以句柄操作时尽量用with(file打开操作,网络套接字)


# 代码续行
print(
    """
    dfadfadfkfoe
    dfadfadfad23
    """
)
string = (
    "hfkajdfladjf'ak,"
    "hjfe;55646adfadf"
)


# 不需要的变量用占位符'_'接收


# 链式比较
a = 15
if 10 < a < 20:
    print('hello')
# 等价于
if a > 10 and a < 20:
    print('hello')


# 三目运算
a = 10
b = 100 if a > 2 else 200
# 等价于
if a > 2:
    b = 100
else:
    b = 200


# 字典合并
a = {1: 'a'}
b = {2: 'b'}
c = {**a, **b}


# 字符串反转
s = 'abcdefg'
s[::-1]


# 列表转字符串
l = ['aa', 'bb', 'cc']
L = ' '.join(l)


# 检查列表是否有0,有就提前结束查找,没有就做别的.
foo = [0, 1, 3, 4, 44]
Flag = False
for i in foo:
    if i == 0:
        Flag = True
        break
if not Flag:
    print('ha ha.')
# for else语法实现
for i in foo:
    if i == 0:
        break
else:
    print('ha ha.')


# 赋值表达式(海象运算)3.8版本
import re
data = "hello123world"
match = re.search("(\d+)", data)  # 3
if match:
    num = match.group(1)          # 4
else:
    num = None
# 合并3, 4行
if match:=re.search("(\d+)", data):
    num = match.group(1)
else:
    num = None


# isinstance 判断实例类型
isinstance(1, (int, float))
# 等价
isinstance(1, int) or isinstance(1, float)


# 用http.server共享文件
# python3:   python3 -m http.server
# python2:   python2 -m SimpleHTTPServer 8080


# zip()函数实现字典键值对互换
lang = {"python": ".py", "java": ".java"}
dict(zip(lang.values(), lang.keys()))
# {".java": "java", ".py": "python"}


# 查找列表中出现次数最多的数字
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5]
max(set(test), key=test.count)


# 使用slots节省内存
import sys
class MyClass:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
print(sys.getsizeof(MyClass))
####
class MyClass:
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
print(sys.getsizeof(MyClass))


# 扩展列表
i = ['a', 'b', 'c']
i.extend(['e', 'f', 'g'])


# 二维数组变一维数组
import itertools
a = [[1, 2], [3, 4], [5, 6]]
i = itertools.chain(*a)
list(i)


# 有索引的迭代
a = ['Merry', 'Christmas', 'Day']
for i, x in enumerate(a):
    print('{}: {}'.format(i, x))


## 装饰器 ##
from functools import wraps

def tags(tag_name):
    def tag_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tag_decorator

@tags("P")
def get_text(name):
    """return some text"""
    return "hello " + name

print(get_text("python"))



