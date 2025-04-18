"""
https://www.pythoncheatsheet.org/
python速查表(PEP 20)
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

# python basics
Operators	        Operation	        Example
**	                Exponent	        2 ** 3 = 8
%	                Modulus/Remainder	22 % 8 = 6
//	                Integer division	22 // 8 = 2
/	                Division	        22 / 8 = 2.75
*	                Multiplication	    3 * 3 = 9
-	                Subtraction	        2 = 3
+	                Addition	        2 + 2 = 4

# 复合赋值运算
Operator	Equivalent
spam += 1	spam = spam + 1
spam -= 1	spam = spam - 1
spam *= 1	spam = spam * 1
spam /= 1	spam = spam / 1
spam %= 1	spam = spam % 1

# data type
Data Type	                Examples
Integers	                -2, -1, 0, 1, 2, 3, 4, 5
Floating-point numbers	    -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
Strings	                    'a', 'aa', 'aaa', 'Hello!', '11 cats'

# variables
变量命名规则:
1. 以单个单词命名
2. 可以使用字母,数字,下划线(_)组合
3. 不能以数字开头

# 注释
1. 井号开头或者被三引号包括起来的字符串视为2注释
2. 三引号一般用于函数和类注释

# 常用函数
>>> print('Hello world!')
Hello world!
>>> a = 1
>>> print('Hello world!', a)
Hello world! 1

>>> print('What is your name?')   # ask for their name
>>> myName = input()
>>> print('It is good to meet you, {}'.format(myName))
What is your name?
Al
It is good to meet you, Al

>>> len('hello')
5

# str(), int(), and float() 函数
>>> str(29)
'29'
>>> print('I am {} years old.'.format(str(29)))
I am 29 years old.
>>> str(-3.14)
'-3.14'

>>> int(7.7)
7

测试空字符串,空列表,空字典等,不要使用len()函数,更好的做法:
>>> a = [1, 2, 3]
>>> if a:
>>>     print("the list is not empty!")

## 流程控制
# 比较运算符
Operator	        Meaning
==	                Equal to
!=	                Not equal to
<	                Less than
>	                Greater Than
<=	                Less than or Equal to
>=	                Greater than or Equal to

# 布尔运算
不要使用 == 或 != 运算符来评估布尔运算,使用is或is not运算符
>>> True == True   # 不推荐
True
>>> True != False  # 不推荐
True

>>> True is True       # 推荐
True
>>> True is not False  # 推荐
True

# 以下语句等同
>>> if a is True:
>>>    pass
>>> if a is not False:
>>>    pass
>>> if a:
>>>    pass

# 更好的写法
>>> if a is False:
>>>    pass
>>> if a is not True:
>>>    pass
>>> if not a:
>>>    pass

# 布尔操作符
Expression	            Evaluates to
True and True	        True
True and False	        False
False and True	        False
False and False	        False
True or True	        True
True or False	        True
False or True	        True
False or False	        False
not True	            False
not False	            True

# 混合布尔运算和比较运算,甚至表达式混合
>>> (4 < 5) and (5 < 6)
True
>>> (4 < 5) and (9 < 6)
False
>>> (1 == 2) or (2 == 2)
True

>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True

# in 和 not in操作符
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True

>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False

>>> 'cat' not in spam
True

# if语句
if name == 'Alice':
    print('Hi, Alice.')

# else 语句
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

# elif 语句
name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')

name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

# while循环
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# break 语句(终止循环)
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue语句(跳过本次循环,进入下一循环)
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# for循环和range()函数
>>> print('My name is')
>>> for i in range(5):
>>>     print('Jimmy Five Times ({})'.format(str(i)))
My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)

range()函数可以调用三个参数,前两个参数是开始和结束值,第三个参数是步长值
>>> for i in range(0, 10, 2):
>>>    print(i)
0
2
4
6
8

>>> for i in range(5, -1, -1):
>>>     print(i)
5
4
3
2
1
0

# for else语句
>>> for i in [1, 2, 3, 4, 5]:
>>>    if i == 3:
>>>        break
>>> else:
>>>    print("only executed when no item of the list is equal to 3")

# import modules
import random
for i in range(5):
    print(random.randint(1, 10))

import random, sys, os, math

from random import *

# 使用sys.exit()结束程序
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed {}.'.format(response))

# 自定义函数
>>> def hello(name):
>>>     print('Hello {}'.format(name))
>>>
>>> hello('Alice')
>>> hello('Bob')
Hello Alice
Hello Bob

# 返回值和返回语句
- 关键字return
- 要返回的值或者表达式
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# None值
>>> spam = print('Hello!')
Hello!
>>> spam is None
True
注意:不要使用==来跟None比较,总是使用is运算

# print()和关键字参数
>>> print('Hello', end='')
>>> print('World')
HelloWorld

>>> print('cats', 'dogs', 'mice')
cats dogs mice

>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice

# 局部和全局作用域
- 全局范围内的代码不能使用任何局部变量
- 但是，局部作用域可以访问全局变量
- 函数局部作用域内的代码变量不能在其他任何局部作用域内使用
- 在不同的作用域内的变量可以使用相同的名字，比如局部作用域内有一个spam的变量，全局作用域内也可以有一个spam变量

# global语句
- 如果您需要在函数中修改全局变量，请使用全局语句：
>>> def spam():
>>>     global eggs
>>>     eggs = 'spam'
>>>
>>> eggs = 'global'
>>> spam()
>>> print(eggs)
spam

# 共有四个规则来判断变量是在局部范围内还是在全局范围内：
- 如果在全局范围内（即，在所有函数之外）使用变量，则该变量始终是全局变量
- 如果函数中存在该变量的全局语句(global)，则它是全局变量
- 另外，如果该变量在函数的参数语句中使用，则它是局部变量
- 但是，如果该变量未在参数语句中使用，则它是全局变量

# 异常处理
>>> def spam(divideBy):
>>>     try:
>>>         return 42 / divideBy
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>
>>> print(spam(2))
>>> print(spam(12))
>>> print(spam(0))
>>> print(spam(1))
21.0
3.5
Error: Invalid argument: division by zero
None
42.0

>>> def spam(divideBy):
>>>     try:
>>>         return 42 / divideBy
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>     finally:
>>>         print("-- division finished --")
>>> print(spam(2))
-- division finished --
21.0
>>> print(spam(12))
-- division finished --
3.5
>>> print(spam(0))
Error: Invalid Argument division by zero
-- division finished --
None
>>> print(spam(1))
-- division finished --
42.0

# 列表
>>> spam = ['cat', 'bat', 'rat', 'elephant']

>>> spam
['cat', 'bat', 'rat', 'elephant']

# 索引
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2]
'rat'
>>> spam[3]
'elephant'
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'

>>> 'The {} is afraid of the {}.'.format(spam[-1], spam[-3])
'The elephant is afraid of the bat.'

# 切片
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']

>>> spam2 = spam[:]
['cat', 'bat', 'rat', 'elephant']
>>> spam.append('dog')
>>> spam
['cat', 'bat', 'rat', 'elephant', 'dog']
>>> spam2
['cat', 'bat', 'rat', 'elephant']

# 改变列表中的值
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'

>>> spam
['cat', 'aardvark', 'rat', 'elephant']

>>> spam[2] = spam[1]

>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']

>>> spam[-1] = 12345

>>> spam
['cat', 'aardvark', 'aardvark', 12345]

# 列表串联和列表复制
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']

>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

>>> spam = [1, 2, 3]

>>> spam = spam + ['A', 'B', 'C']

>>> spam
[1, 2, 3, 'A', 'B', 'C']

# 删除列表中的值
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']

>>> del spam[2]
>>> spam
['cat', 'bat']

# for循环遍历列表
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i, supply in enumerate(supplies):
>>>     print('Index {} in supplies is: {}'.format(str(i), supply))
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders

# 使用zip()遍历多个列表
>>> name = ['Pete', 'John', 'Elizabeth']
>>> age = [6, 23, 44]
>>> for n, a in zip(name, age):
>>>     print('{} is {} years old'.format(n, a))
Pete is 6 years old
John is 23 years old
Elizabeth is 44 years old

# 解包
>>> cat = ['fat', 'orange', 'loud']

>>> size, color, disposition = cat

# 交换两个变量的值
>>> a, b = 'Alice', 'Bob'
>>> a, b = b, a

# 在列表中查找元素的索引
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

>>> spam.index('Pooka')
1

# 往列表中追加,插入,移除元素
>>> spam = ['cat', 'dog', 'bat']

>>> spam.append('moose')

>>> spam
['cat', 'dog', 'bat', 'moose']

>>> spam = ['cat', 'dog', 'bat']

>>> spam.insert(1, 'chicken')

>>> spam
['cat', 'chicken', 'dog', 'bat']

>>> spam = ['cat', 'bat', 'rat', 'elephant']

>>> spam.remove('bat')

>>> spam
['cat', 'rat', 'elephant']
注意:如果该元素在列表中出现多次，则只会移除第一次出现的实例

# sort()排序列表
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]

>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']

>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> sorted(spam)
['ants', 'badgers', 'cats', 'dogs', 'elephants']

# 元组数据类型
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'

>>> eggs[1:3]
(42, 0.5)

>>> len(eggs)
3

注意：元组与列表不同的主要是元组（如字符串）是不可变的

# 使用list()和tuple()函数转换类型
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)

>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]

>>> list('hello')
['h', 'e', 'l', 'l', 'o']

# 字典
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# keys(), values(), and items()方法
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
>>>     print(v)
red
42

>>> for k in spam.keys():
>>>     print(k)
color
age

>>> for i in spam.items():
>>>     print(i)
('color', 'red')
('age', 42)

>>> spam = {'color': 'red', 'age': 42}
>>>
>>> for k, v in spam.items():
>>>     print('Key: {} Value: {}'.format(k, str(v)))
Key: age Value: 42
Key: color Value: red

# 检查字典中是否存在键或值
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True

>>> 'Zophie' in spam.values()
True

>>> # You can omit the call to keys() when checking for a key
>>> 'color' in spam
False

>>> 'color' not in spam
True

# get()方法： 具有两个参数：键和默认值
>>> picnic_items = {'apples': 5, 'cups': 2}

>>> 'I am bringing {} cups.'.format(str(picnic_items.get('cups', 0)))
'I am bringing 2 cups.'

>>> 'I am bringing {} eggs.'.format(str(picnic_items.get('eggs', 0)))
'I am bringing 0 eggs.'

# setdefault()方法
spam = {'name': 'Pooka', 'age': 5}
思考如下代码:
if 'color' not in spam:
    spam['color'] = 'black'

更简洁的做法
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'

>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}

>>> spam.setdefault('color', 'white')
'black'

>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}

# 美观的printing
>>> import pprint
>>>
>>> message = 'It was a bright cold day in April, and the clocks were striking
>>> thirteen.'
>>> count = {}
>>>
>>> for character in message:
>>>     count.setdefault(character, 0)
>>>     count[character] = count[character] + 1
>>>
>>> pprint.pprint(count)
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}

# 合并两个字典
# in Python 3.5+:
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = {**x, **y}
>>> z
{'c': 4, 'a': 1, 'b': 3}

# in Python 2.7
>>> z = dict(x, **y)
>>> z
{'c': 4, 'a': 1, 'b': 3}

# 集合sets
- 集合是没有重复元素的无序集合。 基本用途包括成员资格测试和消除重复条目。 集合对象还支持数学运算，例如并集，交集，差和对称差。
- 初始化集合
>>> s = {1, 2, 3}
>>> s = set([1, 2, 3])

- 创建空集时，请确保不要使用大括号{}，否则您将获得一个空字典
>>> s = {}
>>> type(s)
<class 'dict'>

- 去重
>>> s = {1, 2, 3, 2, 3, 4}
>>> s
{1, 2, 3, 4}

- 并且作为无序数据类型，无法对其进行索引
>>> s = {1, 2, 3}
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>>

- add() and update() discard()方法
>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}

>>> s = {1, 2, 3}
>>> s.update([2, 3, 4, 5, 6])
>>> s
{1, 2, 3, 4, 5, 6}  # remember, sets automatically remove duplicates

>>> s = {1, 2, 3}
>>> s.discard(3)
>>> s
{1, 2}
>>> s.discard(3)
>>>

- union() or |
>>> s1 = {1, 2, 3}
>>> s2 = {3, 4, 5}
>>> s1.union(s2)  # or 's1 | s2'
{1, 2, 3, 4, 5}

- intersection() or &
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s3 = {3, 4, 5}
>>> s1.intersection(s2, s3)  # or 's1 & s2 & s3'

- difference() or -
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1.difference(s2)  # or 's1 - s2'
{1}
>>> s2.difference(s1) # or 's2 - s1'
{4}

- symetric_difference() or ^
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1.symmetric_difference(s2)  # or 's1 ^ s2'
{1, 4}

# intertools模块
- itertools模块是一个工具集合，目的是在处理迭代器(如列表或字典)时快速并有效地使用内存
- 该模块标准化了一组快速、高效内存的核心工具，这些工具本身或组合起来都很有用。它们一起构成了一个迭代器代数，使得用纯Python简洁而高效地构造专门的工具成为可能

- 创建一个返回函数结果的迭代器
import itertools
itertools.accumulate(iterable[, func])

>>> data = [1, 2, 3, 4, 5]
>>> result = itertools.accumulate(data, operator.mul)
>>> for each in result:
>>>    print(each)
1
2
6
24
120

- operator.mul取两个数并将它们相乘
operator.mul(1, 2)
2
operator.mul(2, 3)
6
operator.mul(6, 4)
24
operator.mul(24, 5)
120

- 只传递可迭代序列不传递函数,则汇总所有项
>>> data = [5, 2, 6, 4, 5, 9, 1]
>>> result = itertools.accumulate(data)
>>> for each in result:
>>>    print(each)
5
7
13
17
22
31
32
- 过程如下
5
5 + 2 = 7
7 + 6 = 13
13 + 4 = 17
17 + 5 = 22
22 + 9 = 31
31 + 1 = 32

- 接受一个可迭代的整数.这将创建具有r成员的所有唯一组合
itertools.combinations(iterable, r)

>>> shapes = ['circle', 'triangle', 'square',]
>>> result = itertools.combinations(shapes, 2)
>>> for each in result:
>>>    print(each)
('circle', 'triangle')
('circle', 'square')
('triangle', 'square')

- 与combination()类似，但允许单个元素重复多次
itertools.combinations_with_replacement(iterable, r)

>>> shapes = ['circle', 'triangle', 'square']
>>> result = itertools.combinations_with_replacement(shapes, 2)
>>> for each in result:
>>>    print(each)
('circle', 'circle')
('circle', 'triangle')
('circle', 'square')
('triangle', 'triangle')
('triangle', 'square')
('square', 'square')

- 创建一个迭代器，返回从start号开始的等距值
itertools.count(start=0, step=1)

>>> for i in itertools.count(10,3):
>>>    print(i)
>>>    if i > 20:
>>>        break
10
13
16
19
22

- cycle()在迭代器中无休止地循环
itertools.cycle(iterable)

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
>>> for color in itertools.cycle(colors):
>>>    print(color)
red
orange
yellow
green
blue
violet
red
orange

- 获取一系列可迭代对象，并将它们作为一个长可迭代对象返回
itertools.chain(*iterables)

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
>>> shapes = ['circle', 'triangle', 'square', 'pentagon']
>>> result = itertools.chain(colors, shapes)
>>> for each in result:
>>>    print(each)
red
orange
yellow
green
blue
circle
triangle
square
pentagon

- 过滤一个可迭代的对象
itertools.compress(data, selectors)

>>> shapes = ['circle', 'triangle', 'square', 'pentagon']
>>> selections = [True, False, True, False]
>>> result = itertools.compress(shapes, selections)
>>> for each in result:
>>>    print(each)
circle
square

- 创建一个迭代器，只要谓词为真，就从可迭代对象中删除元素;然后，返回每个元素
itertools.dropwhile(predicate, iterable)

>>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
>>> result = itertools.dropwhile(lambda x: x<5, data)
>>> for each in result:
>>>    print(each)
5
6
7
8
9
10
1

- 使一个迭代器从可迭代的元素中筛选出仅返回谓词为False的元素
itertools.filterfalse(predicate, iterable)

>>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
>>> result = itertools.filterfalse(lambda x: x<5, data)
>>> for each in result:
>>>    print(each)
5
6
7
8
9
10

- groupby()函数将一些事物组合在一起
itertools.groupby(iterable, key=None)

>>> robots = [{
    'name': 'blaster',
    'faction': 'autobot'
}, {
    'name': 'galvatron',
    'faction': 'decepticon'
}, {
    'name': 'jazz',
    'faction': 'autobot'
}, {
    'name': 'metroplex',
    'faction': 'autobot'
}, {
    'name': 'megatron',
    'faction': 'decepticon'
}, {
    'name': 'starcream',
    'faction': 'decepticon'
}]
>>> for key, group in itertools.groupby(robots, key=lambda x: x['faction']):
>>>    print(key)
>>>    print(list(group))
autobot
[{'name': 'blaster', 'faction': 'autobot'}]
decepticon
[{'name': 'galvatron', 'faction': 'decepticon'}]
autobot
[{'name': 'jazz', 'faction': 'autobot'}, {'name': 'metroplex', 'faction': 'autobot'}]
decepticon
[{'name': 'megatron', 'faction': 'decepticon'}, {'name': 'starcream', 'faction': 'decepticon'}]

- islice()函数与切片很相似,允许对iterable进行切片
itertools.islice(iterable, start, stop[, step])

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue',]
>>> few_colors = itertools.islice(colors, 2)
>>> for each in few_colors:
>>>    print(each)
red
orange

- itertools.permutations(iterable, r=None)

>>> alpha_data = ['a', 'b', 'c']
>>> result = itertools.permutations(alpha_data)
>>> for each in result:
>>>    print(each)
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')

- 从一系列可迭代对象创建笛卡尔乘积。
>>> num_data = [1, 2, 3]
>>> alpha_data = ['a', 'b', 'c']
>>> result = itertools.product(num_data, alpha_data)
>>> for each in result:
    print(each)
(1, 'a')
(1, 'b')
(1, 'c')
(2, 'a')
(2, 'b')
(2, 'c')
(3, 'a')
(3, 'b')
(3, 'c')

- 此功能将一遍又一遍地重复一个对象指定次数
itertools.repeat(object[, times])

>>> for i in itertools.repeat("spam", 3):
    print(i)
spam
spam
spam

- 创建一个迭代器，从迭代器中取出元素作为参数传递给函数
itertools.starmap(function, iterable)

>>> data = [(2, 6), (8, 4), (7, 3)]
>>> result = itertools.starmap(operator.mul, data)
>>> for each in result:
>>>    print(each)
12
32
21

- 与dropwhile（）相反。 创建一个迭代器，并在谓词为true时从迭代器返回元素
itertools.takewhile(predicate, iterable)

>>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
>>> result = itertools.takewhile(lambda x: x<5, data)
>>> for each in result:
>>>    print(each)
1
2
3
4

- 从单个可迭代对象返回n个独立的迭代器。
itertools.tee(iterable, n=2)

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
>>> alpha_colors, beta_colors = itertools.tee(colors)
>>> for each in alpha_colors:
>>>    print(each)
red
orange
yellow
green
blue

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
>>> alpha_colors, beta_colors = itertools.tee(colors)
>>> for each in beta_colors:
>>>    print(each)
red
orange
yellow
green
blue

- 创建一个迭代器，该迭代器聚合每个可迭代对象中的元素。 如果可迭代项的长度不均匀，则将缺失值填充为fillvalue。 迭代一直持续到最长的可迭代耗尽为止
itertools.zip_longest(*iterables, fillvalue=None)

>>> colors = ['red', 'orange', 'yellow', 'green', 'blue',]
>>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
>>> for each in itertools.zip_longest(colors, data, fillvalue=None):
>>>    print(each)
('red', 1)
('orange', 2)
('yellow', 3)
('green', 4)
('blue', 5)
(None, 6)
(None, 7)
(None, 8)
(None, 9)
(None, 10)

## 推导式

# 列表推导式
>>> a = [1, 3, 5, 7, 9, 11]

>>> [i - 1 for i in a]
[0, 2, 4, 6, 8, 10]

# 集合推导式
>>> b = {"abc", "def"}
>>> {s.upper() for s in b}
{"ABC", "DEF"}

# 字典推导式
>>> c = {'name': 'Pooka', 'age': 5}
>>> {v: k for k, v in c.items()}
{'Pooka': 'name', 5: 'age'}

# 可以从字典生成列表推导式
>>> c = {'name': 'Pooka', 'first_name': 'Oooka'}
>>> ["{}:{}".format(k.upper(), v.upper()) for k, v in c.items()]
['NAME:POOKA', 'FIRST_NAME:OOOKA']

# 字符串操作
Escape character	Prints as
\'	                Single quote
\"	                Double quote
\t	                Tab
\n	                Newline (line break)
\\	                Backslash

- example：
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.

- 原始字符串完全忽略所有转义字符并打印字符串中出现的任何反斜杠
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.

- 三引号多行字符串
>>> print('''Dear Alice,
>>>
>>> Eve's cat has been arrested for catnapping, cat burglary, and extortion.
>>>
>>> Sincerely,
>>> Bob''')
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob

- 为了使代码保持更好，可以使用textwrap标准包中的dedent函数。
>>> from textwrap import dedent
>>>
>>> def my_function():
>>>     print('''
>>>         Dear Alice,
>>>
>>>         Eve's cat has been arrested for catnapping, cat burglary, and extortion.
>>>
>>>         Sincerely,
>>>         Bob
>>>         ''').strip()

- 索引和切片字符串
>>> spam = 'Hello world!'

>>> spam[0]
'H'

>>> spam[4]
'o'

>>> spam[-1]
'!'

>>> spam[0:5]
'Hello'

>>> spam[:5]
'Hello'

>>> spam[6:]
'world!'

>>> spam[6:-1]
'world'

>>> spam[:-1]
'Hello world'

>>> spam[::-1]
'!dlrow olleH'

>>> spam = 'Hello world!'
>>> fizz = spam[0:5]
>>> fizz
'Hello'

- upper(), lower(), isupper(), and islower()方法

>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'

>>> spam = spam.lower()
>>> spam
'hello world!'

>>> spam = 'Hello world!'
>>> spam.islower()
False

>>> spam.isupper()
False

>>> 'HELLO'.isupper()
True

>>> 'abc12345'.islower()
True

>>> '12345'.islower()
False

>>> '12345'.isupper()
False

- 如果字符串只包含字母且不为空，则isalpha()返回True

- isalnum()如果字符串只包含字母和数字且不为空，则返回True

- 如果字符串只包含数字字符且不为空，则isdecimal()返回True

- 如果字符串仅包含空格，制表符和换行符，并且不为空白，则isspace()返回True

- 如果字符串只包含以大写字母开头后跟小写字母的单词，则istitle()返回True。

- startswith() and endswith() 方法

>>> 'Hello world!'.startswith('Hello')
True

>>> 'Hello world!'.endswith('world!')
True

>>> 'abc123'.startswith('abcdef')
False

>>> 'abc123'.endswith('12')
False

>>> 'Hello world!'.startswith('Hello world!')
True

>>> 'Hello world!'.endswith('Hello world!')
True

-  join() and split()方法

>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'

>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'

>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']

>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']

>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

- rjust(), ljust(), and center()方法

>>> 'Hello'.rjust(10)
'     Hello'

>>> 'Hello'.rjust(20)
'               Hello'

>>> 'Hello World'.rjust(20)
'         Hello World'

- rjust()和ljust()的第二个可选参数将指定填充字符而不是空格字符。在交互式shell中输入以下内容

>>> 'Hello'.rjust(20, '*')
'***************Hello'

>>> 'Hello'.ljust(20, '-')
'Hello---------------'

>>> 'Hello'.center(20)
'       Hello 

>>> 'Hello'.center(20, '=')
'=======Hello========'

- strip(), rstrip(), and lstrip()方法

>>> spam = '    Hello World     '
>>> spam.strip()
'Hello World'

>>> spam.lstrip()
'Hello World '

>>> spam.rstrip()
'    Hello World'

>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'

- 使用pyperclip模块复制和粘贴字符串(需要pip安装)

>>> import pyperclip

>>> pyperclip.copy('Hello world!')

>>> pyperclip.paste()
'Hello world!'

- 字符串格式化

>>> name = 'Pete'
>>> 'Hello %s' % name
"Hello Pete"

可以使用%x格式说明符将int值转换为字符串
>>> num = 5
>>> 'I have %x apples' % num
"I have 5 apples"

- 强烈建议使用str.format或f-strings (Python 3.6+)而不是%操作符。

>>> name = 'John'
>>> age = 20'

>>> "Hello I'm {}, my age is {}".format(name, age)
"Hello I'm John, my age is 20"

>>> "Hello I'm {0}, my age is {1}".format(name, age)
"Hello I'm John, my age is 20"

>>> name = 'Elizabeth'
>>> f'Hello {name}!'
'Hello Elizabeth!

- 内联算术
>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
'Five plus ten is 15 and not 30.'

- 模版字串，这是一种更简单但功能不那么强大的机制，但是在处理用户生成的格式字符串时推荐使用它。由于模板字符串的复杂度较低，所以它是一个更安全的选择。

>>> from string import Template
>>> name = 'Elizabeth'
>>> t = Template('Hey $name!')
>>> t.substitute(name=name)
'Hey Elizabeth!'

# 正则表达式
1. 导入模块 import re
2. 使用re.compile()函数(使用原始字符串)创建一个正则对象
3. 传递一个字符串给正则对象的search()方法,这会返回一个匹配对象
4. 调用匹配对象的group()方法返回一个实际字符串或者匹配到的文本

- 匹配正则对象
>>> import re
>>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> print('Phone number found: {}'.format(mo.group()))
Phone number found: 415-555-4242

- Grouping with Parentheses
>>> phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'

- 要一次获取所有组:使用groups()方法，注意名称的复数形式
>>> mo.groups()
('415', '555-4242')
>>> area_code, main_number = mo.groups()
>>> print(area_code)
415
>>> print(main_number)
555-4242

- 使用管道获取多组，|字符被称为管道。你可以在任何你想匹配许多表达式中的一个的地方使用它。例如，正则表达式r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
>>> hero_regex = re.compile (r'Batman|Tina Fey')
>>> mo1 = hero_regex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'
>>> mo2 = hero_regex.search('Tina Fey and Batman.')
>>> mo2.group()
'Tina Fey'

- 还可以使用管道来匹配作为regex一部分的几种模式之一
>>> bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = bat_regex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile

- ?字符将其前面的组标记为模式的可选部分。
>>> bat_regex = re.compile(r'Bat(wo)?man')
>>> mo1 = bat_regex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = bat_regex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

- *(称为星号或星号)表示匹配零或更多，在星号之前的组可以在文本中出现任意次数
>>> bat_regex = re.compile(r'Bat(wo)*man')
>>> mo1 = bat_regex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = bat_regex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>> mo3 = bat_regex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'

- *表示匹配零或多个，+(或+)表示匹配一个或多个。加号前面的组必须至少出现一次
>>> bat_regex = re.compile(r'Bat(wo)+man')
>>> mo1 = bat_regex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = bat_regex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = bat_regex.search('The Adventures of Batman')
>>> mo3 is None
True

- 用花括号匹配特定的重复次数

>>> ha_regex = re.compile(r'(Ha){3}')
>>> mo1 = ha_regex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

>>> mo2 = ha_regex.search('Ha')
>>> mo2 is None
True

- 贪婪和非贪婪模式匹配(Python的正则表达式默认情况下是贪婪的，这意味着在有歧义的情况下，它们将匹配尽可能长的字符串。花括号的非贪婪版本，它匹配最短的字符串，有右花括号，后跟一个问号)

>>> greedy_ha_regex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedy_ha_regex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'

-  findall()方法，除了search()方法之外，Regex对象还有一个findall()方法。虽然search()将返回搜索字符串中第一个匹配文本的匹配对象，但findall()方法将返回搜索字符串中每个匹配的字符串

>>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

要总结findall()方法返回的结果，请记住以下内容
1.当在没有组的正则表达式上调用时，比如\d-\d\d\d-\d\d\d, findall()方法会返回一个ng匹配的列表，比如['415-555-9999'，'212-555-0000']。
2.在具有组的regex上调用时，例如(\d\d\d)-(d\d)-(d\d\d\d)， findall()方法返回字符串的e列表(每个组一个字符串)，例如[('415'，'555'，'9999')，('212'，'555'，'0000')]。

- 有时您想匹配一组字符，但是速记字符类(\d、\w、\s等等)太宽泛了。您可以使用方括号定义自己的字符类。例如，字符类[aeiouAEIOU]将匹配任何元音，包括小写和大写
>>> vowel_regex = re.compile(r'[aeiouAEIOU]')
>>> vowel_regex.findall('Robocop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

- 还可以使用连字符来包含字母或数字的范围。例如，字符类[a-zA-Z0-9]将匹配所有的小写字母、大写字母和数字。
- 通过在字符类的左括号后面放置一个插入符号(^)，您可以创建一个负字符类。否定字符类将匹配所有不在该字符类中的字符。例如，在交互式shell中输入以下内容
>>> consonant_regex = re.compile(r'[^aeiouAEIOU]')
>>> consonant_regex.findall('Robocop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

- 您还可以在正则表达式的开头使用插入符号(^)来表示匹配必须出现在搜索文本的开头
- 同样，您可以在正则表达式的末尾放一个美元符号(\$)，以表示字符串必须以这个正则表达式模式结束。
- 并且你可以一起使用^和\$来表示整个字符串必须匹配正则表达式，也就是说，仅仅匹配字符串的某个子集是不够的

>>> begins_with_hello = re.compile(r'^Hello')
>>> begins_with_hello.search('Hello world!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> begins_with_hello.search('He said hello.') is None
True

- 正则表达式字符串r'\d\$'匹配以0到9的数字字符结尾的字符串
>>> whole_string_is_num = re.compile(r'^\d+$')
>>> whole_string_is_num.search('1234567890')
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
>>> whole_string_is_num.search('12345xyz67890') is None
True
>>> whole_string_is_num.search('12 34567890') is None
True

- 通配符字符(正则表达式中的(点)字符称为通配符，它将匹配除换行符以外的任何字符)
>>> at_regex = re.compile(r'.at')
>>> at_regex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']

- 用.*来匹配所有东西
>>> name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = name_regex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'

>>> mo.group(2)
'Sweigart'

- 点星号使用贪婪模式:它总是尝试匹配尽可能多的文本。要以一种非贪婪的方式匹配任何和所有文本，请使用点、星号和问号(.*?)问号告诉Python以非贪婪的方式匹配
>>> nongreedy_regex = re.compile(r'<.*?>')
>>> mo = nongreedy_regex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'

>>> greedy_regex = re.compile(r'<.*>')
>>> mo = greedy_regex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'

- 用点字符匹配换行符(点星号将匹配除换行符以外的所有内容。通过将re.DOTALL作为re.compile()的第二个参数传递，可以使点字符匹配所有字符，包括换行字符)
>>> no_newline_regex = re.compile('.*')
>>> no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'

>>> newline_regex = re.compile('.*', re.DOTALL)
>>> newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# Regex符号
Symbol	                        Matches
?	                            zero or one of the preceding group.
*	                            zero or more of the preceding group.
+	                            one or more of the preceding group.
{n}	                            exactly n of the preceding group.
{n,}	                        n or more of the preceding group.
{,m}	                        0 to m of the preceding group.
{n,m}	                        at least n and at most m of the preceding p.
{n,m}? or *? or +?	            performs a nongreedy match of the preceding p.
^spam	                        means the string must begin with spam.
spam$	                        means the string must end with spam.
.	                            any character, except newline characters.
\d, \w, and \s	                a digit, word, or space character, respectively.
\D, \W, and \S	                anything except a digit, word, or space, respectively.
[abc]	                        any character between the brackets (such as a, b, ).
[^abc]	                        any character that isn’t between the brackets.

- 不区分大小写的匹配(要使你的正则不区分大小写，你可以传递re.IGNORECASE或re.I作为re.compile()的第二个参数)
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'

>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

- sub()方法,正则对象的sub()方法传递两个参数，第一个参数是一个字符串，用于替换任何匹配项，第二个是用于正则表达式的字符串，sub()方法返回一个应用了替换的字符串
>>> names_regex = re.compile(r'Agent \w+')

>>> names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.

另一个例子：
>>> agent_names_regex = re.compile(r'Agent (\w)\w*')

>>> agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
A**** told C**** that E**** knew B**** was a double agent.'

- 要告诉re.compile()函数忽略正则表达式字符串中的空格和注释，可以通过将re.VERBOSE变量作为re.compile()的第二个参数来启用verbose模式。

- 您可以使用像这样的注释将正则表达式扩展到多行
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# 文件和目录路径处理
- Python中有两个主要模块处理路径操作。一个os.path路径模块，另一个是pathlib模块。pathlib模块是在Python 3.4中添加的，提供了一种面向对象的方式来处理文件系统路径。
- 反斜杠(\)在Windows上，正斜杠(/)在OS X和Linux上
- 如果您的代码需要在不同的平台上工作，那么连接路径可能是一个令人头疼的问题。
- 幸运的是，Python提供了简单的方法来处理这个问题。我们将展示如何使用os.path来处理这个问题。连接和pathlib.Path.joinpath

在windows上使用os.path.join
>>> import os

>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'

类unix上使用pathlib
>>> from pathlib import Path

>>> print(Path('usr').joinpath('bin').joinpath('spam'))
usr/bin/spam

- pathlib也提供一种便捷的方式
>>> from pathlib import Path

>>> print(Path('usr') / 'bin' / 'spam')
usr/bin/spam

- 请注意，基于Windows和基于Unix的操作系统之间的路径分隔符是不同的，这就是为什么您希望使用上述方法之一，而不是将字符串添加到一起来连接路径
- 如果您需要在同一个目录下创建不同的文件路径，那么连接路径是有帮助的

在windows上使用os.path.join
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']

>>> for filename in my_files:
>>>     print(os.path.join('C:\\Users\\asweigart', filename))
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx

在类unix上使用pathlib
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
>>> home = Path.home()
>>> for filename in my_files:
>>>     print(home / filename)
/home/asweigart/accounts.txt
/home/asweigart/details.csv
/home/asweigart/invite.docx

- 当前工作目录
windows上使用os
>>> import os

>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')

>>> os.getcwd()
'C:\\Windows\\System32'

类unix上使用patlib
>>> from pathlib import Path
>>> from os import chdir

>>> print(Path.cwd())
/home/asweigart

>>> chdir('/usr/lib/python3.6')
>>> print(Path.cwd())
/usr/lib/python3.6

- 创建一个新的目录
使用os模块windows上
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')

使用pathlib类unix上
>>> from pathlib import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/pathlib.py", line 1226, in mkdir
    self._accessor.mkdir(self, mode)
  File "/usr/lib/python3.6/pathlib.py", line 387, in wrapped
    return strfunc(str(pathobj), *args)
FileNotFoundError: [Errno 2] No such file or directory: '/home/asweigart/delicious/walnut/waffles'

- 我们有一个严重的错误!原因是'delicious'目录不存在，所以我们不能在它下面创建'walnut'和'waffles'目录。要解决这个问题:
>>> from pathlib import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)

# 绝对路径与相对路径
使用os.path在类unix上
>>> import os
>>> os.path.isabs('/')
True
>>> os.path.isabs('..')
False

使用pathlib在类unix上
>>> from pathlib import Path
>>> Path('/').is_absolute()
True
>>> Path('..').is_absolute()
False

- 使用os.path或pathlib提取绝对路径
>>> import os
>>> os.getcwd()
'/home/asweigart'
>>> os.path.abspath('..')
'/home'

from pathlib import Path
print(Path.cwd())
/home/asweigart
print(Path('..').resolve())
/home

- 相对路径
 >>> import os
>>> os.path.relpath('/etc/passwd', '/')
'etc/passwd'

>>> from pathlib import Path
>>> print(Path('/etc/passwd').relative_to('/'))
etc/passwd

- 检查路径的正确性
import os
>>> os.path.exists('.')
True
>>> os.path.exists('setup.py')
True
>>> os.path.exists('/etc')
True
>>> os.path.exists('nonexistentfile')
False

from pathlib import Path
>>> Path('.').exists()
True
>>> Path('setup.py').exists()
True
>>> Path('/etc').exists()
True
>>> Path('nonexistentfile').exists()
False

- 检查是否是文件
>>> import os
>>> os.path.isfile('setup.py')
True
>>> os.path.isfile('/home')
False
>>> os.path.isfile('nonexistentfile')
False

>>> from pathlib import Path
>>> Path('setup.py').is_file()
True
>>> Path('/home').is_file()
False
>>> Path('nonexistentfile').is_file()
False

- 检查是否是目录
>>> import os
>>> os.path.isdir('/')
True
>>> os.path.isdir('setup.py')
False
>>> os.path.isdir('/spam')
False

>>> from pathlib import Path
>>> Path('/').is_dir()
True
>>> Path('setup.py').is_dir()
False
>>> Path('/spam').is_dir()
False

- 查询文件大小和目录内容
>>> import os
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192

>>> from pathlib import Path
>>> stat = Path('/bin/python3.6').stat()
>>> print(stat) # stat contains some other information about the file as well
os.stat_result(st_mode=33261, st_ino=141087, st_dev=2051, st_nlink=2, st_uid=0,
--snip--
st_gid=0, st_size=10024, st_atime=1517725562, st_mtime=1515119809, st_ctime=1517261276)
>>> print(stat.st_size) # size in bytes
10024

>>> import os
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

>>> from pathlib import Path
>>> for f in Path('/usr/bin').iterdir():
>>>     print(f)
...
/usr/bin/tiff2rgba
/usr/bin/iconv
/usr/bin/ldd
/usr/bin/cache_restore
/usr/bin/udiskie
/usr/bin/unix2dos
/usr/bin/t1reencode
/usr/bin/epstopdf
/usr/bin/idle3
...

>>> import os
>>> total_size = 0

>>> for filename in os.listdir('C:\\Windows\\System32'):
      total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

>>> print(total_size)
1117846456

>>> from pathlib import Path
>>> total_size = 0

>>> for sub_path in Path('/usr/bin').iterdir():
...     total_size += sub_path.stat().st_size
>>>
>>> print(total_size)
1903178911

- 文件和目录拷贝
>>> import shutil, os

>>> os.chdir('C:\\')

>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
   'C:\\delicious\\spam.txt'

>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
   'C:\\delicious\\eggs2.txt'

- 虽然shutil.copy()将复制单个文件，但shutil.copytree()将复制整个文件夹以及其中包含的每个文件夹和文件
>>> import shutil, os

>>> os.chdir('C:\\')

>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'

- 移动和重命名文件和文件名
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'

- 目标路径也可以指定一个文件名。在下面的示例中，源文件将被移动并重命名
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'

- 如果没有eggs文件夹，那么move()将把bacon.txt重命名为一个名为eggs的文件。
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'

- 永久删除文件和目录
1.调用os.unlink(path)或path .unlink()将删除路径上的文件
2.调用os.rmdir(path)或path. rmdir()将删除path上的文件夹。该文件夹必须为空的任何文件或文件夹
3.调用shutil.rmtree(path)将删除path中的文件夹，它包含的所有文件和文件夹也将被删除。

- 使用send2trash模块安全删除(在终端窗口运行pip install send2trash来安装这个模块)
>>> import send2trash

>>> with open('bacon.txt', 'a') as bacon_file: # creates the file
...     bacon_file.write('Bacon is not a vegetable.')
25

>>> send2trash.send2trash('bacon.txt')

- 遍历目录
>>> import os
>>>
>>> for folder_name, subfolders, filenames in os.walk('C:\\delicious'):
>>>     print('The current folder is {}'.format(folder_name))
>>>
>>>     for subfolder in subfolders:
>>>         print('SUBFOLDER OF {}: {}'.format(folder_name, subfolder))
>>>     for filename in filenames:
>>>         print('FILE INSIDE {}: {}'.format(folder_name, filename))
>>>
>>>     print('')
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt

- pathlib提供了比上面列出的更多的功能，如获取文件名，获取文件扩展名，读写文件

- 文件读写
>>> with open('C:\\Users\\your_home_folder\\hello.txt') as hello_file:
...     hello_content = hello_file.read()
>>> hello_content
'Hello World!'

>>> # Alternatively, you can use the *readlines()* method to get a list of string values from the file, one string for each line of text:

>>> with open('sonnet29.txt') as sonnet_file:
...     sonnet_file.readlines()
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']

>>> # You can also iterate through the file line by line:
>>> with open('sonnet29.txt') as sonnet_file:
...     for line in sonnet_file: # note the new line character will be included in the line
...         print(line, end='')

When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,

- 写文件
>>> with open('bacon.txt', 'w') as bacon_file:
...     bacon_file.write('Hello world!\n')
13

>>> with open('bacon.txt', 'a') as bacon_file:
...     bacon_file.write('Bacon is not a vegetable.')
25

>>> with open('bacon.txt') as bacon_file:
...     content = bacon_file.read()

>>> print(content)
Hello world!
Bacon is not a vegetable.

- 用shelve模块保存变量
>>> import shelve

>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> with shelve.open('mydata') as shelf_file:
...     shelf_file['cats'] = cats

- 打开并读取变量
>>> with shelve.open('mydata') as shelf_file:
...     print(type(shelf_file))
...     print(shelf_file['cats'])
<class 'shelve.DbfilenameShelf'>
['Zophie', 'Pooka', 'Simon']

- 就像字典一样，shelf值也有keys()和values()方法，它们将返回shelf上键和值的类似列表的值。由于这些方法返回的是类似列表的值，而不是真正的列表，所以应该将它们传递给list()函数以获得列表形式的值。
>>> with shelve.open('mydata') as shelf_file:
...     print(list(shelf_file.keys()))
...     print(list(shelf_file.values()))
['cats']
[['Zophie', 'Pooka', 'Simon']]

- 使用print.pformat()函数保存变量
>>> import pprint

>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"

>>> with open('myCats.py', 'w') as file_obj:
...     file_obj.write('cats = {}\n'.format(pprint.pformat(cats)))
83

- 读取zip文件
>>> os.chdir('C:\\')    # move to the folder with example.zip
>>> with zipfile.ZipFile('example.zip') as example_zip:
...     print(example_zip.namelist())
...     spam_info = example_zip.getinfo('spam.txt')
...     print(spam_info.file_size)
...     print(spam_info.compress_size)
...     print('Compressed file is %sx smaller!' % (round(spam_info.file_size / spam_info.compress_size, 2)))

['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
13908
3828
'Compressed file is 3.63x smaller!'

- 从zip文件中中提取文件
用于ZipFile对象的extractall()方法将ZIP文件中的所有文件和文件夹提取到当前工作目录中
>>> import zipfile, os

>>> os.chdir('C:\\')    # move to the folder with example.zip

>>> with zipfile.ZipFile('example.zip') as example_zip:
...     example_zip.extractall()

ZipFile对象的extract()方法将从ZIP文件中提取单个文件。继续交互式shell示例：
>>> with zipfile.ZipFile('example.zip') as example_zip:
...     print(example_zip.extract('spam.txt'))
...     print(example_zip.extract('spam.txt', 'C:\\some\\new\\folders'))
'C:\\spam.txt'
'C:\\some\\new\\folders\\spam.txt'

- 创建zip文件(这段代码将创建一个名为new. ZIP的新ZIP文件，其中包含spam.txt的压缩内容。)
>>> import zipfile

>>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
...     new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

# json，yaml和配置文件
- 打开一个json文件
import json
with open("filename.json", "r") as f:
    content = json.loads(f.read())

- 往json文件中写内容
import json

content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:
    f.write(json.dumps(content, indent=2))

- 与JSON相比，YAML提供了更好的可维护性，并允许您添加注释。对于需要手工编辑的配置文件来说，这是一个方便的选择
- 有两个主要的库允许访问YAML文件：PyYaml和Ruamel.yaml。使用pip安装它们；第一个更容易使用，而第二个Ruamel更好地实现了YAML规范，例如，允许在不修改注释的情况下修改YAML内容

- 打开一个yaml文件
from ruamel.yaml import YAML

with open("filename.yaml") as f:
    yaml=YAML()
    yaml.load(f)

- anyconfig模块是一个非常方便的包，它允许完全抽象底层配置文件格式。它允许从JSON、YAML、TOML等加载Python字典(pip install anyconfig)
usage:
import anyconfig

conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")

# 调试
- 抛出异常
- 异常由raise语句引发。在代码中，raise语句由以下内容组成：
1.raise关键字
2.对Exception()函数的调用
3.传递给Exception()函数的有用错误消息的字符串

>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.

- 通常是调用函数的代码，而不是函数本身，知道如何处理异常。因此，你通常会在函数中看到raise语句，在调用函数的代码中看到try和except语句。
def box_print(symbol, width, height):
    if len(symbol) != 1:
      raise Exception('Symbol must be a single character string.')
    if width <= 2:
      raise Exception('Width must be greater than 2.')
    if height <= 2:
      raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

#获取作为字符串的回溯信息
每当引发的异常未得到处理时，Python就会显示回溯信息。但也可以通过调用traceback来获取它作为字符串。格式exc()。如果您想要从异常的回溯得到信息，但又想用except语句优雅地处理异常，那么这个函数是很有用的。在调用此函数之前，您需要导入Python的traceback模块。
>>> import traceback

>>> try:
>>>      raise Exception('This is the error message.')
>>> except:
>>>      with open('errorInfo.txt', 'w') as error_file:
>>>          error_file.write(traceback.format_exc())
>>>      print('The traceback info was written to errorInfo.txt.')
116
The traceback info was written to errorInfo.txt.
- 116是write()方法的返回值，因为向文件写入了116个字符。回溯文本被写入errorInfo.txt。

Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
Exception: This is the error message.

# 断言
断言是一种健全性检查，以确保代码没有出现明显的错误。这些健全性检查由assert语句执行。如果完整性检查失败，则引发AssertionError异常。在代码中，assert语句由以下内容组成：
1. assert关键字
2. 条件(即计算结果为True或False的表达式)
3. 逗号
4. 当条件为False时显示的字符串

>>> pod_bay_door_status = 'open'

>>> assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

>>> pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'

>>> assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".

- 用简单的英语说，断言语句说，我断言这个条件为真，如果不为真，说明程序中的某个地方有错误。与异常不同，你的代码不应该使用try和except来处理断言语句;如果一个断言失败，你的程序应该崩溃.
- 通过像这样的快速失败，您缩短了从最初引起错误的原因到第一次注意到错误之间的时间。这将减少在找到导致错误的代码之前必须检查的代码数量。
- 禁用断言,在运行Python时，可以通过传递-O选项来禁用断言

# logging
要使日志记录模块能够在程序运行时在屏幕上显示日志消息，请将以下内容复制到程序顶部
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

- 假设你写了一个函数来计算一个数的阶乘。在数学中，4的阶乘是1 2 3 4，或者24。7的阶乘是1 2 3 4 5 6 7，或者5,040。打开一个新的文件编辑器窗口，输入以下代码。它有一个bug，但是您还需要输入一些日志消息来帮助自己找出问题出在哪里。将程序保存为factorial allog .py。
>>> import logging
>>>
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
>>>
>>> logging.debug('Start of program')
>>>
>>> def factorial(n):
>>>
>>>     logging.debug('Start of factorial(%s)' % (n))
>>>     total = 1
>>>
>>>     for i in range(1, n + 1):
>>>         total *= i
>>>         logging.debug('i is ' + str(i) + ', total is ' + str(total))
>>>
>>>     logging.debug('End of factorial(%s)' % (n))
>>>
>>>     return total
>>>
>>> print(factorial(5))
>>> logging.debug('End of program')
2015-05-23 16:20:12,664 - DEBUG - Start of program
2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
0
2015-05-23 16:20:12,684 - DEBUG - End of program

- logging级别，日志级别提供了一种按重要性对日志消息进行分类的方法。有五种日志级别。可以使用不同的日志功能在每个级别记录消息
Level	    Logging Function	Description
DEBUG	    logging.debug()	    The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
INFO	    logging.info()  	Used to record information on general events in your program or confirm that things are working at their point in the program.
WARNING	    logging.warning()	Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
ERROR	    logging.error()	    Used to record an error that caused the program to fail to do something.
CRITICAL	logging.critical()	The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

- 禁用loggin,在调试了程序之后，您可能不希望所有这些日志消息使屏幕混乱。disable()函数将禁用这些功能，这样您就不必进入程序并手动删除所有的日志记录调用。
>>> import logging

>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')

>>> logging.critical('Critical error! Critical error!')
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!

>>> logging.disable(logging.CRITICAL)

>>> logging.critical('Critical error! Critical error!')

>>> logging.error('Error! Error!')

- logging to file
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 匿名函数
>>> add = lambda x, y: x + y
>>> add(5, 3)
8

- 不需要绑定到一个名称上
>>> (lambda x, y: x + y)(5, 3)
8

- 与常规嵌套函数一样，lambda也作为词法闭包工作
>>> def make_adder(n):
        return lambda x: x + n

>>> plus_3 = make_adder(3)
>>> plus_5 = make_adder(5)

>>> plus_3(4)
7
>>> plus_5(4)
9

- lambda只能计算表达式，就像一行代码。

- 许多编程语言都有一个三元操作符，它定义了一个条件表达式。最常见的用法是做一个简短的条件赋值语句。换句话说，如果条件为真，它提供一行代码来计算第一个表达式，否则它计算第二个表达式。
<expression1> if <condition> else <expression2>

>>> age = 15

>>> print('kid' if age < 18 else 'adult')
kid

- 三元运算符可以链接
>>> age = 15

>>> print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')
teenager

- 上面的代码等价于:
if age < 18:
    if age < 13:
        print('kid')
    else:
        print('teenager')
else:
    print('adult')

# args and kwargs

- args和kwargs的名称是任意的——重要的是*和**操作符。他们可以是
1. 在函数声明中，*表示将所有剩余的位置参数打包到一个名为<name>的元组中，而**对于关键字参数也是一样的(除了它使用的是字典，而不是元组)。
2. 在函数调用中，*表示将元组或名为<name>的列表解包到此位置的位置参数，而**对于关键字参数也是一样的

- 创建一个可以用来调用任何其他函数的函数，不管它有什么参数
def forward(f, *args, **kwargs):
    return f(*args, **kwargs)

- 在forward内部，args是一个元组(除了第一个位置参数f，因为我们指定了它)，kwargs是一个字典。然后调用f并解包它们，使它们成为f的普通参数。
- 当有数量不定的位置参数时，可以使用*args。
>>> def fruits(*args):
>>>    for fruit in args:
>>>       print(fruit)

>>> fruits("apples", "bananas", "grapes")

"apples"
"bananas"
"grapes"

- 类似地，当关键字参数的数量不确定时，可以使用**kwargs
>>> def fruit(**kwargs):
>>>    for key, value in kwargs.items():
>>>        print("{0}: {1}".format(key, value))

>>> fruit(name = "apple", color = "red")

name: apple
color: red

>>> def show(arg1, arg2, *args, kwarg1=None, kwarg2=None, **kwargs):
>>>   print(arg1)
>>>   print(arg2)
>>>   print(args)
>>>   print(kwarg1)
>>>   print(kwarg2)
>>>   print(kwargs)

>>> data1 = [1,2,3]
>>> data2 = [4,5,6]
>>> data3 = {'a':7,'b':8,'c':9}

>>> show(*data1,*data2, kwarg1="python",kwarg2="cheatsheet",**data3)
1
2
(3, 4, 5, 6)
python
cheatsheet
{'a': 7, 'b': 8, 'c': 9}

>>> show(*data1, *data2, **data3)
1
2
(3, 4, 5, 6)
None
None
{'a': 7, 'b': 8, 'c': 9}

# If you do not specify ** for kwargs
>>> show(*data1, *data2, *data3)
1
2
(3, 4, 5, 6, "a", "b", "c")
None
None
{}

- 注意事项：
1. 函数可以通过在def语句中使用*args接受数量可变的位置参数
2. 可以使用序列中的项作为带有*操作符的函数的位置参数
3. 使用*操作符和生成器可能会导致程序内存不足和崩溃
4. 向接受*args的函数添加新的位置参数可能会引入难以发现的错误
5. 函数参数可以通过位置或关键字来指定
6. 关键字清楚地说明了每个参数的目的是什么，当它与位置参数混淆时
7. 带有默认值的关键字参数可以很容易地向函数添加新的行为，特别是当函数有现有的调用者时。
8. 可选关键字参数应该总是通过关键字而不是位置来传递

# 上下文管理
- 虽然Python的上下文管理器被广泛使用，但很少有人理解其使用背后的目的。这些语句通常用于读写文件，通过确保特定的资源只用于特定的进程，帮助应用程序节约系统内存和改进资源管理
- 例如，文件对象是上下文管理器。当上下文结束时，文件对象将自动关闭
>>> with open(filename) as f:
>>>     file_contents = f.read()

# the open_file object has automatically been closed.
- 结束块执行的任何事情都会导致上下文管理器的退出方法被调用.这包括异常，当错误导致您过早退出打开的文件或连接时，这些异常非常有用.
- 退出脚本时，没有正确地关闭文件或连接描述符是糟糕的，这可能导致数据丢失或者一些其它的问题.通过使用上下文管理器，您可以确保始终采取预防措施，以防止以这种方式造成的损害或丢失

- 使用生成器语法编写自己的contextmanager，多亏了contextlib，还可以使用生成器语法编写上下文管理器。contextmanager装饰
>>> import contextlib
>>> @contextlib.contextmanager
... def context_manager(num):
...     print('Enter')
...     yield num + 1
...     print('Exit')
>>> with context_manager(2) as cm:
...     # the following instructions are run when the 'yield' point of the context
...     # manager is reached.
...     # 'cm' will have the value that was yielded
...     print('Right in the middle with cm = {}'.format(cm))
Enter
Right in the middle with cm = 3
Exit

# __main__,顶层脚本的运行环境
- __main__ 是顶级代码执行的作用域的名称,当从标准输入、脚本或交互式提示符读取时，模块的名称被设置为__main__
- 模块可以通过检查自己的名称来发现它是否在__main__作用域中运行，这允许在模块作为脚本或使用python -m运行时有条件地执行代码，但在模块被导入时不执行
>>> if __name__ == "__main__":
...     # execute only if run as a script
...     main()

- 对于一个包，可以通过包含main.py模块来实现同样的效果，当使用-m运行该模块时，会执行main.py模块的内容
- 例如，我们正在开发的脚本被设计成作为模块使用，我们应该这样做
>>> # Python program to execute function directly
>>> def add(a, b):
...     return a+b
...
>>> add(10, 20) # we can test it by calling the function save it as calculate.py
30
>>> # Now if we want to use that module by importing we have to comment out our call,
>>> # Instead we can write like this in calculate.py
>>> if __name__ == "__main__":
...     add(3, 5)
...
>>> import calculate
>>> calculate.add(3, 5)
8

- 注意
1. 每个Python模块都定义了自己的名称，如果它是main，就意味着该模块是由用户独立运行的，我们可以执行相应的适当操作
2. 如果将此脚本作为模块导入到另一个脚本中，则名称将设置为脚本/模块的名称。
3. Python文件既可以作为可重用模块，也可以作为独立程序
4. if __name__ == '__main__':仅在文件被直接运行而未导入时，才用于执行某些代码。

# setup.py
- 在使用Distutils构建、分发和安装模块时，安装脚本是所有活动的中心。安装脚本的主要目的是将您的模块分发给Distutils，以便对您的模块进行操作的各种命令能够正确执行
- setup.py文件是Python项目的核心。它描述了有关项目的所有元数据。您可以将许多字段添加到项目中，以提供丰富的描述项目的元数据集。但是，只有三个必填字段：名称，版本和软件包。
- 如果要在Python软件包索引（PyPI）上发布软件包，则名称字段必须唯一。版本字段跟踪项目的不同发行版。软件包字段描述了您在项目中放置Python源代码的位置。

python setup.py install

- 我们的初始setup.py还将包括有关许可证的信息，并将重用README.txt文件作为长描述字段。这看起来像
>>> from distutils.core import setup
>>> setup(
...    name='pythonCheatsheet',
...    version='0.1',
...    packages=['pipenv',],
...    license='MIT',
...    long_description=open('README.txt').read(),
... )

- 等多信息访问:http://docs.python.org/install/index.html.

# dataclasses
- 数据类是python类，但适合存储数据对象。此模块提供了一个装饰器和函数，用于自动将生成的特殊方法(如init()和repr())添加到用户定义的类中。
- 特征
1. 它们存储数据并表示某种数据类型。例:一个数字。对于熟悉ORMs的人来说，模型实例就是一个数据对象。它代表一种特定的实体。它持有定义或表示实体的属性。
2. 它们可以与同类型的其他对象进行比较。一个数字可以大于、小于或等于另一个数字

- Python 3.7提供了一个装饰器数据类，用于将一个类转换为一个数据类。
>>> @dataclass
... class Number:
...     val: int
...
>>> obj = Number(2)
>>> obj.val
2

- python2.7
>>> class Number:
...     def __init__(self, val):
...         self.val = val
...
>>> obj = Number(2)
>>> obj.val
2

- 默认值
- 向数据类的字段添加默认值
>>> @dataclass
... class Product:
...     name: str
...     count: int = 0
...     price: float = 0.0
...
>>> obj = Product("Python")
>>> obj.name
Python
>>> obj.count
0
>>> obj.price
0.0

- 类型提示
- 必须在数据类中定义数据类型。但是，如果您不想指定数据类型，那么使用typing.Any
>>> from dataclasses import dataclass
>>> from typing import Any

>>> @dataclass
... class WithoutExplicitTypes:
...    name: Any
...    value: Any = 42

# 虚拟环境
- 使用虚拟环境是为了在封装的环境中测试python代码，同时也避免用可能只用于一个项目的库填充基本的python安装

- install virtualenv
pip install virtualenv

- install  virtualenvwrapper-win
pip install virtualenvwrapper-win

- usage
mkvirtualenv HelloWold

- 要将我们的virtualenv绑定到当前的工作目录，只需输入
setprojectdir .

- 要移动到命令行中的其他内容，请键入deactivate以禁用您的环境
deactivate

- 打开命令提示符并输入workon HelloWold以激活环境并移动到您的根项目文件夹
workon HelloWold

- poetry是Python中依赖项管理和打包的工具。 它允许您声明项目所依赖的库，它将为您管理（安装/更新）它们。
pip install --user poetry

- 创建一个新的项目
poetry new my-project

my-project
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py

pyproject.toml文件将编排您的项目及其依赖项
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["your name <your@mail.com>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"

- 要向项目添加依赖项，可以在tool.poetry.dependencies部分指定它们
[tool.poetry.dependencies]
pendulum = "^1.4"

- 另外，不用修改pyproject。您可以使用add命令，它将自动找到合适的版本约束。
$ poetry add pendulum

- 安装pyproject.toml中列出的依赖项
poetry install

- 移除依赖项
poetry remove pendulum

- 更多请参考: https://python-poetry.org/docs/

# pipenv
- Pipenv是一个工具，旨在将最好的所有包装世界(bundler, composer, npm, cargo, yarn等)带入Python世界。Windows是我们这个世界的一流公民
pip install pipenv

- 输入项目目录并安装项目的包
cd my_project
pipenv install <package>

- Pipenv将安装您的包，并在项目的s目录中为您创建一个Pipfile。Pipfile用于跟踪项目需要哪些依赖项，以防需要重新安装它们
卸载包
pipenv uninstall <package>

- 激活与Python项目关联的虚拟环境
pipenv shell

- 退出虚拟环境
exit

# anaconda
- Anaconda是另一个流行的管理python包的工具。

- 创建一个虚拟环境
conda create -n HelloWorld

- 激活虚拟环境
conda activate HelloWorld

-退出虚拟环境
conda deactivate
"""

