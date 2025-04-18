# -*-coding:utf-8-*-
"""
collections模块包含除内置内型list,dict,和tuple以外的其他容器数据类型
"""
import collections


# ChainMap支持与常规字典相同的API来访问现有的值
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

# 按字典映射传递到构造函数的顺序来搜索(即m['c'] == 'C')
m = collections.ChainMap(a, b)
print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))

# 重排
print(m.maps)
print('c = {}\n'.format(m['c']))
# Reverse the list
m.maps = list(reversed(m.maps))
print(m.maps)
print('c = {}\n'.format(m['c']))

# 更新值,ChainMap不会缓存映射中的值,更改源map值会反映到ChainMap中,在ChainMap中修改映射值也会反映到源映射的第一个映射中
n = collections.ChainMap(a, b)
print('Before: {}'. format(n['c']))
a['c'] = 'M'
print('After: {}'.format(n['c']))

# ChainMap可以用一个额外的映射在maps列表的最前面创建一个新的实例.这样可以避免修改现有的底层数据结构
c = {'a': 'A', 'c': 'C'}
d = {'b': 'B', 'c': 'D'}
e = collections.ChainMap(c, d)
f = e.new_child()

print('e before:', e)
print('f before:', f)
f['c'] = 'E'
print('e before:', e)
print('f before:', f)
