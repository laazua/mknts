"""
当前app目录下执行: pdm run celery -A celery_worker worker -l info
"""
import os
import celery
from celery import platforms


platforms.C_FORCE_ROOT = True


# 获取环境变量
rds_host = os.getenv("rds_host", "172.17.0.1")
rds_port = os.getenv("rds_port", 6379)
rds_db_1 = os.getenv("rds_db_1", 1)
rds_db_2 = os.getenv("rds_db_2", 2)


# celery配置
celery_app = celery.Celery(__name__, include=[
    'tasks.zone_task', 'tasks.host_task'])
celery_app.conf.broker_url = f"redis://{rds_host}:{rds_port}/{rds_db_1}"
celery_app.conf.result_backend = f"redis://{rds_host}:{rds_port}/{rds_db_2}"


#######################################获取结果#########################################
from tasks import celery_app
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
