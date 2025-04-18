"""
当前目录执行: pdm run celery -A celery_tasks worker -l info
"""
from celery_tasks import celery_app
from celery.result import AsyncResult


# 获取结果
def get_celery_result(ids):
    results = []
    for id in ids:
        result = AsyncResult(id=id, app=celery_app)
        if result.successful():
            results.append(result.get())
        if result.failed():
            results.append(f"{id}执行失败")
        if result.status == 'PENDING':
            results.append(f"{id}任务等待被执行")
        if result.status == 'RETRY':
            results.append(f"{id}任务稍后重试")
        if result.status == 'STARTED':
            results.append(f"{id}任务已经执行")
    return results
