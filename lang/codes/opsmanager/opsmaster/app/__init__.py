import typing
import celery
from celery.result import AsyncResult

from app.config import AppConfig
from app.applog import AppLogger


celery_app = celery.Celery(
    "celery task", 
    include=["app.tasks.zone"]
)
celery_app.conf.broker_url = "redis://{0}:{1}/{2}".format(
    AppConfig.get("redis", "host"),
    AppConfig.get("redis", "port"),
    AppConfig.get("redis", "broker")
)
celery_app.conf.result_backend = "redis://{0}:{1}/{2}".format(
    AppConfig.get("redis", "host"),
    AppConfig.get("redis", "port"),
    AppConfig.get("redis", "backend")
)


def get_task_result(ids: typing.List[typing.Any]) -> typing.List[typing.Any]:
    """获取task结果"""
    data = []
    for id in ids:
        result = AsyncResult(id=f"{id}", app=celery_app)
        if result.successful():
            data.append(result.get())
        if result.failed():
            data.append(f"{id} 任务执行失败!")
        if result.status == "PENDING":
            data.append(f"{id} 任务正在执行中...")
        if result.status == "RETRY":
            data.append(f"{id} 任务稍后重试!")
    # return [AsyncResult(id=f"{id}", app=celery_app).get() for id in ids]
    return data


__all__ = [
    AppConfig, AppLogger, celery_app, get_task_result
]
