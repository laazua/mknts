"""
启动worker: ../.venv/bin/celery -A celery_tasks worker -l info --pool threads
"""
import celery


celery_app = celery.Celery(
    'celery_app',
    broker='redis://127.0.0.1:6379/1',
    backend='redis://127.0.0.1:6379/2',
    include=['celery_tasks.task01', 'celery_tasks.task02'])


# 时区
celery_app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
celery_app.conf.enable_utc = False
