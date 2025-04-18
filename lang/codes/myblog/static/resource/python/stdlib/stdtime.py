"""
time模块表示时间的3种方式:
  - 时间戳
  - 结构化时间对象
  - 格式化时间字符串
"""
import time


# 时间戳 1970.1.1到指定时间的时间间隔(单位秒)
time_stamp = time.time()
print(time_stamp)


# 结构化时间对象
st = time.localtime()
print(st)
print(st[0])


# 格式化时间字符串
ct = time.ctime()
print(ct)
st = time.strftime("%Y-%m-%d %H:%M:%S %A %B %W %w")
print(st)