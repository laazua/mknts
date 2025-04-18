import time
from celery_tasks import celery_app


@celery_app.task
def host_option(ip: str):
    time.sleep(5)
    return ip
