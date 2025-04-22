### re

- **示例**
```python
import re


strings = "2334dbad12kjmlL89nNDK90Ll2ddd"

# re.match
# 从字符串的起始位置开始匹配正则表达式模式。如果匹配成功，返回一个匹配对象；否则，返回None
result = re.match(r"\d+", strings)
if result:
    print(result.group())


# re.search
# 扫描整个字符串，查找第一个匹配正则表达式模式的子串。如果找到，返回一个匹配对象；否则，返回None
result = re.search(r"\d+", strings)
if result:
    print(result.group())


# re.findall
result = re.findall(r"\d+", strings)
if result:
    print(result)


# re.finditer
result = re.finditer(r"\d+", strings)
if result:

    print([res.group() for res in result])


# re.sub
# 将匹配到的字符串进行替换
result = re.sub(r"\d+", "##", strings)
print(result)


# re.subn
# 将匹配到的字符串进行替换,返回一个元组
result = re.subn(r"\d+", "##", strings)
print(result)


# re.split
# 按照指定的匹配模式分隔字符串
result = re.split(r"\d+", strings)
print(result)


# re.compile 获取一个正则表达式对象 
pattern = re.compile(r"\d+")
print(pattern.match(strings).group())
print(pattern.search(strings).group())
print(pattern.findall(strings))
print(pattern.sub("##", strings))
```