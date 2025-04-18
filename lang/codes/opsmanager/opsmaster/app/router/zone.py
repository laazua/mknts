from fastapi import APIRouter, Depends
from app import core, tasks, schema, AppLogger, get_task_result


task_ids = []
router = APIRouter(prefix="/api", tags=["区服接口"])


@router.post("/zone", description="区服操作接口OK")
async def option(post: schema.OptZone) -> core.AppResponse:
    # 区服信息入库
    print("xxx", post)
    target = post.zone[0].target
    if  target == "addition" and not core.zone_db_add(post.zone):
        return core.AppResponse(40000, message="区服信息入库失败")

    # 区服远程操作
    if task_ids:
        task_ids.clear()
    for z in post.zone:
        zone = {
            "name": z.name,
            "number": z.number,
            "ip": z.ip,
            "target": z.target,
            "svnversion": z.svnversion
        }
        task = tasks.call_zone_service.delay(zone)
        task_ids.append(task)

    return core.AppResponse(20000, message=f"{target}区服成功")


@router.get("/zone", description="操作结果接口OK")
async def result() -> core.AppResponse:
    data = get_task_result(task_ids)
    if not data:
        AppLogger.error("未获取到tasks结果")
        return core.AppResponse(20000, message="获取tasks结果失败")
    return core.AppResponse(20000, message="获取tasks结果成功", data=data)


@router.get("/zones", description="区服列表接口")
async def list(
    # token_data = Depends(core.get_current_user)
) -> core.AppResponse:
    data = core.zone_db_lst()
    if not data:
        return core.AppResponse(40000, message="获取区服列表失败")
    return core.AppResponse(20000, data=data)
