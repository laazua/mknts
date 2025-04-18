# -*- coding: utf-8 -*-
# 系统用户接口模块

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.common import  get_current_user
from app import schemas
from app.service.user import result_router_info 
from app.service.user import result_user_info
from app.service.user import result_user_register
from app.service.user import result_user_login


router = APIRouter(prefix='/user/api', tags=['用户接口'])


@router.post('/login')
async def login(req: OAuth2PasswordRequestForm = Depends()):
    """用户认证接口"""
    return await result_user_login(req)


@router.get('/userinfo')
async def get_user_info(token_data: schemas.TokenData = Depends(get_current_user)):
    return await result_user_info(token_data)
    

@router.post('/register')
async def register(req: schemas.UserDb, _: schemas.TokenData = Depends(get_current_user)):
    """用户注册接口"""
    return await result_user_register(req)


@router.get('/router')
async def get_router(_: schemas.TokenData = Depends(get_current_user)):
    return await result_router_info()


@router.get('/userlist')
async def get_user_list(req: schemas.User, _:schemas.TokenData = Depends(get_current_user)):
    """用户列表接口"""
    pass
