from fastapi import APIRouter
from celery.result import AsyncResult
from app.internal import schema
from app.internal.core import AppResponse
from app import celery_app
from app.tasks.zone import call_zone_service


task_ids = []
router = APIRouter(prefix="/api", tags=["区服API"])


@router.post("/zone", description="区服操作接口")
async def option(post: schema.OptZone):
    if task_ids:
        task_ids.clear()
    for zone in post.zone:
        z = {
            "zid": zone.zid,
            "zname": zone.zname,
            "zip": zone.zip,
            "target": zone.target,
            "zsvnversion": zone.zsvnversion
        }
        zresult = call_zone_service.delay(z)
        task_ids.append(zresult)
    return AppResponse(20000, msg="区服操作成功")


@router.get("/get", description="操作结果接口")
async def result():
    data = []
    for id in task_ids:
        data.append(AsyncResult(id=f"{id}", app=celery_app).get())
    return AppResponse(20000, msg="获取结果成功", data=data)
