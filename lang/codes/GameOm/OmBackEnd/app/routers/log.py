from fastapi import APIRouter, Depends
from internal.utils import Response, get_current_user
from internal.db.log import log_db


router = APIRouter(prefix="/log/api", tags=["log api"])


@router.get("/log", description="api ok")
async def log(name: str, token_data = Depends(get_current_user)):
    logs = log_db.get(name)
    if not logs:
        return Response(40000, msg="get log failed")
    return Response(20000, data=logs)