from fastapi import APIRouter

from taoist.router import user, role, perm, business


router = APIRouter()

router.include_router(user.router)
router.include_router(role.router)
router.include_router(perm.router)
router.include_router(business.router)
