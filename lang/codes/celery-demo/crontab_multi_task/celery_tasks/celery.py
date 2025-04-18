"""
启动worker: ../.venv/bin/celery -A celery_tasks worker -l info --pool threads -c 4
启动beat: ../.venv/bin/celery -A celery_tasks beat
"""
import celery
from datetime import timedelta


celery_app = celery.Celery(
    'celery_app',
    broker='redis://127.0.0.1:6379/1',
    backend='redis://127.0.0.1:6379/2',
    include=['celery_tasks.task01', 'celery_tasks.task02'])


# 时区
celery_app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
celery_app.conf.enable_utc = False

celery_app.conf.beat_schedule = {
    # 见名知意
    'add-every-10-sec': {
        'task': 'celery_tasks.task01.send_email',
        'schedule': timedelta(seconds=6),
        'args': ('张三',)
    },
    'add-every-15-sec': {
        'task': 'celery_tasks.task02.send_message',
        'schedule': 2.0,
        'args': ('李四',)
    }
}