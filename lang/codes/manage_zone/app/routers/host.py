# @Time:        2022-08-04
# @Author:      Sseve
# @File:        host.py
# @Description: all api of host

from fastapi import APIRouter, BackgroundTasks
from internal.db.host import HostDb
from internal.utils import FabricHandle


router = APIRouter(prefix="/host/api", tags=["host api"])


async def get_host_msg():
    ips = HostDb().get_ips
    _ = [await FabricHandle(ip=ip).get_host_info for ip in set(ips)]


@router.get("/host")
async def host(bg_task: BackgroundTasks):
    """
    Args:
    Return:
    """
    bg_task.add_task(get_host_msg)
    return {"msg": "success"}
