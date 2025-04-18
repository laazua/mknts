import time
from celery_tasks.celery import celery_app


@celery_app.task
def send_email(name):
    print(f"向{name}发送邮件...")
    time.sleep(5)
    print(f"向{name}发送邮件完成.")

    return "ok"
