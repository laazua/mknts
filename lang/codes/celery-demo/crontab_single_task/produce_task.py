from datetime import datetime
from datetime import timedelta
from celery_task import send_email
from celery_task import send_message


## apply_async()中的参数eta存在则是定时任务,eta参数不存在是异步任务

# 方式一[指定时间执行任务]
v1 = datetime(2023, 1, 6, 12, 18, 00)
print(v1)
v2 = datetime.utcfromtimestamp(v1.timestamp())
print(v2)
result = send_email.apply_async(args=["张三"], eta=v2)


# 方式二[相对时间执行]
ctime = datetime.now()
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(minutes=1)
task_time = utc_ctime + time_delay
result = send_message.apply_async(args=["李四"], eta=task_time)
