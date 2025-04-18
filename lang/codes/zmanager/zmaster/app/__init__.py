import celery
from app.config import cfg


# celery配置
celery_app = celery.Celery(
    __name__,
    include=[
        "app.tasks.zone"
    ]
)
celery_app.conf.broker_url = "redis://{0}:{1}/{2}".format(
    cfg.get('redis', 'host'),
    cfg.get('redis', 'port'),
    cfg.get('redis', 'broker'),
)
celery_app.conf.result_backend = "redis://{0}:{1}/{2}".format(
    cfg.get('redis', 'host'),
    cfg.get('redis', 'port'),
    cfg.get('redis', 'backend'),
)


__all__ = [
   cfg, celery_app
]
