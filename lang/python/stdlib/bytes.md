### bytes

- **示例**
```python
# bytes

data = b'hello'
print(data)

print(bytes(10))
print(bytes())
print(bytes([23, 65, 66, 67]))

# 字符串转bytes
s = "zhangsan"
print(s.encode("utf-8"))
# bytes转字符串
print(data.decode("utf-8"))
```