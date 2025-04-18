from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from taoist.core import crud
from taoist.core import security
from taoist.core.models import Token
from taoist.core.deps import SessionDep, current_active_user
from taoist.core.config import settings


router = APIRouter(prefix="/user", tags=["用户操作"])


@router.post("/user/login")
async def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    用户登陆
    """
    user = crud.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.app_expire_time)
    return Token(
        access_token=security.create_token(user.id, expires_delta=access_token_expires)
    )


@router.post(
    "/signout",
    dependencies=[Depends(current_active_user)],
)
async def signout():
    """
    用户登出
    """


@router.post(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def addition():
    """
    用户注册
    """


@router.delete(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def delete():
    """
    用户清除
    """


@router.put(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def update():
    """
    用户更新
    """


@router.get(
    "/",
    dependencies=[Depends(current_active_user)],
)
async def query():
    """
    用户查询
    """
