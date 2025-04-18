from celery_tasks import celery_app
from internal.grpc import call_zone_service


@celery_app.task
def zone_option(zone):
    return call_zone_service(zone)
