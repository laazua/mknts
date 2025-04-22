### struct

- **示例**
```python
import struct


# pack(fmt, v1, v2, ...)：根据格式字符串fmt，将给定的值v1, v2, ...打包成字节串
print(struct.pack("if", 2, 2.5))


# 根据格式字符串fmt，将给定的值v1, v2, ...打包，并写入到buffer的offset位置
buffer = bytearray(8)
struct.pack_into("if", buffer, 0, 1, 2.0)
print(buffer)  # 输出：bytearray(b'\x01\x00\x00\x00\x00\x00\x00@')


strings = "hello"
# 返回字节对象
bytes_strings = struct.pack(f"{len(strings) + 1}p", strings.encode("utf-8"))
print(bytes_strings)


# 创建一个Struct对象，允许多次使用相同的格式进行打包和解包，避免重复编译格式字符串
s = struct.Struct("if")
packed_data = s.pack(1, 2.0)
unpacked_data = s.unpack(packed_data)
print(unpacked_data)  # 输出：(1, 2.0)

```