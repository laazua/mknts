from fastapi import APIRouter, Depends
from internal.db import mongo
from internal.schemas.zone import OptionZone
from internal.core.mlog import logger
from internal.core.result import Response
from tasks import get_celery_result
from tasks.zone_task import zone_option


router = APIRouter(prefix="/api", tags=["区服API"])
_tasks_ids =[]

@router.post("/zone", description="区服操作")
async def opt(post: OptionZone):
    # if post.zone[0].target == "add":
    #     if not mongo.zone_db_add(post.zone):
    #         return Response(40000, msg="区服信息入库失败")
    # 
    # 远程调用(需要多线程)
    if _tasks_ids:
        _tasks_ids.clear()
    for zone in post.zone:
        z = {"name": zone.name, "zid": zone.zid, "domain": zone.domain_name, "target": zone.target}
        result = zone_option.delay(z)
        _tasks_ids.append(result.id)
    return Response(20000, msg="区服操作成功", data=None)


@router.get("/zone_res")
async def opt_res():
    data = get_celery_result(_tasks_ids)
    if not data:
        logger.error("未获取到区服操作结果")
        return Response(40000, msg="未获取到结果")
    logger.info(f"获取区服操作结果成功: {data}")
    return Response(20000, msg="获取区服操作结果成功", data=data)
    


@router.get("/zone", description="区服列表")
async def query():
    zone = mongo.zone_db_get()
    if not zone:
        return Response(40000, msg="获取区服列表失败")
    return Response(20000, msg="获取区服列表成功")