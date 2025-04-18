# -*-coding:utf-8-*-
"""
Counter是一个容器,可以跟踪等效值增加的次数,这个类可以实现其他语言中常用包(bag)或多集合(multiset)数据结构实现的算法
"""
import collections


# Counter 3种初始化方法
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

# 不提供任何参数,构造一个空Counter, 然后通过update()填充
c = collections.Counter()
print('Initial :', c)
c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})  # 数据计数只会增加
print('Dict :', c)

# 访问计数
for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

# elements()返回一个迭代器,该迭代器生成Counter()知道的所有元素
d = collections.Counter('extremely')
d['z'] = 0
print(d)
print(list(d.elements()))

# most_common()

# Counter支持算数操作和集合操作
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('c1:', c1)
print('c2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)
