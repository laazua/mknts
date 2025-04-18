from tasks import celery_app
from internal.grpc import call_zone_service
from internal.core.mlog import logger


@celery_app.task
def zone_option(zone):
    if not zone:
        logger.error("区服信息为空")
        return None        
    return call_zone_service(zone)
