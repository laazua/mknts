# -*- coding: utf-8 -*-
"""业务相关接口"""

from fastapi import APIRouter
from fastapi.param_functions import Depends
from app import schemas
from app.common import get_current_user
from app.service.game import result_zone_list
from app.service.game import result_new_pro
from app.service.game import result_get_pro
from app.service.game import result_open_serve
from app.service.game import result_svn_update
from app.service.game import result_bin_list
from app.service.game import result_bin_host
from app.service.game import result_con_update
from app.service.game import result_zone_start
from app.service.game import result_zone_stop
from app.service.game import result_zone_check
from app.service.game import result_bin_update
from app.service.game import result_host_status


router = APIRouter(prefix='/game/api', tags=['业务接口'])


@router.post('/zonelist')
async def get_zone_list(req: schemas.Zones, _: schemas.TokenData = Depends(get_current_user)):
    """区服列表接口"""
    return await result_zone_list(req)


@router.post('/newpro')
async def new_pro(req: schemas.Project, _: schemas.TokenData = Depends(get_current_user)):
    """新建游戏项目接口"""
    return await result_new_pro(req)


@router.get('/getpro')
async def get_pro(_: schemas.TokenData = Depends(get_current_user)):
    """获取项目接口"""
    return await result_get_pro()


@router.post('/openserve')
async def open_serve(req: schemas.ZoneOpen, _: schemas.TokenData = Depends(get_current_user)):
    """开服接口"""
    return await result_open_serve(req)


@router.post('/zonestart')
async def start_serve(zones: schemas.Zone , _: schemas.TokenData = Depends(get_current_user)):
    """区服启动接口"""
    return await result_zone_start(zones)


@router.post('/zonestop')
async def stop_serve(zones: schemas.Zone , _: schemas.TokenData = Depends(get_current_user)):
    """区服关闭接口"""
    return await result_zone_stop(zones)


@router.post('/confupdate')
async def update_config(zones: schemas.Zone, _: schemas.TokenData = Depends(get_current_user)):
    """配置更新到进程目录接口"""
    return await result_con_update(zones)
    

@router.post('/binupdate')
async def update_bin(zones: schemas.Zone, _: schemas.TokenData = Depends(get_current_user)):
    """bin更新到进程目录接口"""
    return await result_bin_update(zones)


@router.post('/zonecheck')
async def check_serve(zones: schemas.Zone , _: schemas.TokenData = Depends(get_current_user)):
    """区服检查接口"""
    return await result_zone_check(zones)


@router.get('/svnupdate')
async def svn_update(tb: str, cmd: str, _: schemas.TokenData = Depends(get_current_user)):
    """游戏服主机svn更新接口"""
    return await result_svn_update(tb, cmd)


@router.get('/bintohost')
async def bin_to_host(tb: str, cmd: str, _: schemas.TokenData = Depends(get_current_user)):
    return await result_bin_host(tb, cmd)


@router.get('/binlist')
async def get_bin_list(_: schemas.TokenData = Depends(get_current_user)):
    """获取bin文件列表"""
    return await result_bin_list()


@router.get('/hoststatus')
async def get_host_status(tb: str, cmd: str, _: schemas.TokenData = Depends(get_current_user)):
    """获取主机资源接口"""
    return await result_host_status(tb, cmd)