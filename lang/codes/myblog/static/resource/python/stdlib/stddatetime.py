"""
datetime的4个类:
  - date
  - time
  - datetime
  - timedelta
"""
import time
import datetime


print("{:=^50s}".format("datetime.date"))
# date类生成日期(年月日)
print(datetime.date.today()) # 2022-12-31
print(datetime.date(2022, 12, 31)) # 2022-12-31
print(datetime.date.fromtimestamp(time.time())) # 2022-12-31
# date类属性
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution) # timedelta(时间差)
# 实例属性
current_day = datetime.date.today()
print(current_day.year, current_day.month, current_day.day)
# 实例方法
print(current_day.timetuple())
print(current_day.replace(current_day.year, current_day.month, 20))
print(current_day.toordinal())
print(current_day.weekday())
print(current_day.isoweekday())
print(current_day.isoformat())
print(current_day.strftime("%Y-%m-%d"))


print("{:=^50s}".format("datetime.time"))


# time类生成时间(时分秒)
print(datetime.time(16, 36, 55, 666666))
# time类属性
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)
# time实例属性
t = datetime.time(16, 36, 55, 666666)
print(t.hour, t.min, t.second, t.microsecond)
# time实例方法
print(t.isoformat())
print(t.strftime("%H:%M:%S %f"))


print("{:=^50s}".format("datetime.datetime"))


# datetime类生成日期时间
dt = datetime.datetime(2022, 12, 31, 16, 47, 45, 666666)
print(dt)
print(datetime.datetime.today())
print(datetime.datetime.now(tz=None))
print(datetime.datetime.utcnow())
# 时间戳
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)


print("{:=^50s}".format("datetime.timedelta"))


# timedelta类算时间差
td = datetime.timedelta(hours=24)
print(td)
