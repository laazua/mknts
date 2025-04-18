import time
from celery_tasks.celery import celery_app


@celery_app.task
def send_message(name):
    print(f"向{name}发送信息...")
    time.sleep(5)
    print(f"向{name}发送信息完成.")

    return "ok"