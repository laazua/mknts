import typing
from app import celery_app
from app.internal.grpc import zone_service


@celery_app.task
def call_zone_service(
    zone: typing.Dict[str, typing.Any]
) -> typing.Union[typing.Any, None]:
    if not zone:
        return None
    resp = zone_service(zone)
    return {
        "zid": resp.zid,
        "zname": resp.zname,
        "zip": resp.zip,
        "result": resp.result
        }
