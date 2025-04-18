"""
生产者向消息向消息中间件插入消息
运行: ../.venv/bin/python produce_task.py
"""
from celery_task import send_email
from celery_task import send_message


result = send_email.delay("张三")
print(result.id)
result = send_message.delay("李四")
print(result.id)