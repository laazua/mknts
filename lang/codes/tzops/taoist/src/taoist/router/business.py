from fastapi import APIRouter, Depends

from taoist.core.deps import current_active_user


router = APIRouter(prefix="/business", tags=["业务操作"])


@router.post(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def test():
    pass
