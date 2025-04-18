"""
消费者从消息中间件中取消息
../.venv/bin/python consume_task.py
"""
from celery.result import AsyncResult
from celery_tasks.celery import celery_app


# id取自produce_task.py执行结果
result = AsyncResult(id='8258399f-ca00-43dc-bdde-1a3083e236b8', app=celery_app)


if result.successful():
    print(result.get())
if result.failed():
    print("失败")
if result.status == 'PENDING':
    print('任务等待被执行')
if result.status == 'RETRY':
    print('任务异常稍后重试')
if result.status == 'STARTED':
    print('任务已经开始执行')