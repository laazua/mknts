"""
celery -A celery_task worker -l info
"""
import time
import celery


celery_app = celery.Celery(
    "celery_app",
    broker='redis://127.0.0.1:6379/1',
    backend='redis://127.0.0.1:6379/2')


@celery_app.task
def send_email(name):
    print(f"向{name}发送邮件...")
    time.sleep(5)
    print(f"向{name}发送邮件完成.")

    return "ok"


@celery_app.task
def send_message(name):
    print(f"向{name}发送信息...")
    time.sleep(5)
    print(f"向{name}发送信息完成.")

    return "ok"