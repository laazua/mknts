# @Time:        2022-08-04
# @Author:      Sseve
# @File:        zone.py
# @Description: all api of zone

from fastapi import APIRouter, Depends
from internal.models import ZoneAdd
from internal.models import ZoneManage
from internal.db.zone import ZoneDb
from internal.utils import FabricHandle, get_current_user


router = APIRouter(prefix="/zone/api", tags=["zone api"])


@router.post("/zone")
async def zone(zone_list: ZoneAdd, _ = Depends(get_current_user)):
    """
    Args:
        @add => zone arguments like:
            {
                "zones": [
                    {"name":"xxx", "ip":"xxx", "zone_id":1},
                    {"name":"xxx", "ip":"xxx", "zone_id":2}
                ]
            }
    Return:
    """
    # zone info into db
    if not await ZoneDb(zones=zone_list.zones).add:
        return {"code": 400, "msg": "add zone to db failed"}
    zones = [await FabricHandle(zone=zone).add_zone for zone in zone_list.zones]
    print(zones)
    


@router.put("/zone")
async def zone(manage: ZoneManage, _ = Depends(get_current_user)):
    """
    Args:
        @target => action of zone like: [con|bin|start|stop|check|reload]
        @zones => zone arguments like:
            {
                "target":"con",
                "zones": [
                    {"name":"xxx","ip":"xxx", "id":1},
                    {"name":"xxx","ip":"xxx", "id":2}
                ]
            }
    Return:
    """
    print(manage)
