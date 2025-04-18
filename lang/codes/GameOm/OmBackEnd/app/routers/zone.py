# @Time:        2022-08-04
# @Author:      Sseve
# @File:        zone.py
# @Description: all api of zone

from fastapi import APIRouter, Depends
from internal.models import Zone
from internal.db.zone import zone_db
from internal.utils import Response, \
     get_current_user, hand_zone
from internal.db.log import log_db


router = APIRouter(prefix="/zone/api", tags=["zone api"])


@router.get("/zone", description="api ok")
async def zone(token_data = Depends(get_current_user)):
    zone_list = zone_db.get()
    if not zone_list:
        return Response(40000, msg="get zone list failed")
    return Response(20000, data=zone_list)


@router.post("/zone", description="api ok")
async def zone(zone_list: Zone, token_data = Depends(get_current_user)):
    if not log_db.add(name=token_data['username'], action=f"add zone"):
        return Response(40000, msg="add zone log failed")
    # zone info into db
    if not zone_db.add(zone_list):
        return Response(40000, msg="add zone to db failed")
    # result = ZoneHandle(zone=zone_list).action
    result = hand_zone(zone_list)
    if not result:
        return Response(40000, msg="add zone failed")
    return Response(20000, data=result)


@router.put("/zone", description="api ok")
async def zone(manage: Zone, token_data = Depends(get_current_user)):
    if not log_db.add(name=token_data['username'], action=f"{manage.target} zone"):
        return Response(40000, msg=f"{manage.target} zone log failed")
    # result = ZoneHandle(zone=manage).action
    result = hand_zone(manage)
    print(result)
    return Response(20000, data=result)
