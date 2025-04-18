import typing
from app import grpc, celery_app


@celery_app.task
def call_zone_service(
    zone: typing.Dict[str, typing.Any]
) -> typing.Union[typing.Any, None]:
    if not zone:
        return None
    resp =  grpc.zone_service(zone)
    if not resp:
        return {}
    return {"name": resp.name, "number": resp.number, "ip": resp.ip, "result": resp.result}