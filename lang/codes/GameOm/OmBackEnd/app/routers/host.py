# @Time:        2022-08-04
# @Author:      Sseve
# @File:        host.py
# @Description: all api of host

from fastapi import APIRouter, Depends
from internal.db.host import host_db
from internal.utils import Response, \
     get_current_user, hand_host
from internal.db.log import LogDb


router = APIRouter(prefix="/host/api", tags=["host api"])

# token_data = Depends(get_current_user)
@router.get("/host")
async def host():
    # if not LogDb(token_data["username"], f"get host resource").add_log:
    #     return Response(40000, msg="get host msg log failed")
    ips = set(host_db.get_ips())
    # result = HostHandle(ips=ips).resource
    result = hand_host(ips)
    if not result:
        return Response(40000, msg="get None")
    return Response(20000, data=result)
    
