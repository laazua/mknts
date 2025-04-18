"""
当前app目录下执行: pdm run celery -A celery_worker worker -l info
"""
import os
import celery


# 获取环境变量
rds_host = os.getenv("rds_host", "127.0.0.1")
rds_port = os.getenv("rds_port", 6379)
rds_db_1 = os.getenv("rds_db_1", 1)
rds_db_2 = os.getenv("rds_db_2", 2)


# celery配置
celery_app = celery.Celery(__name__, include=[
    'celery_tasks.zone_task', 'celery_tasks.host_task'])
celery_app.conf.broker_url = f"redis://{rds_host}:{rds_port}/{rds_db_1}"
celery_app.conf.result_backend = f"redis://{rds_host}:{rds_port}/{rds_db_2}"
