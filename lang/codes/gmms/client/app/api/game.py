# -*- coding:utf-8 -*-
import concurrent
from fastapi import APIRouter
from fastapi import Depends
from app.libs import schemas, utils, database, resource


router = APIRouter(prefix="/game/api", tags=["Game Api"])


@router.post("/createzones", response_model=schemas.Response, name="zones_tb:create")
async def create_zones(req: schemas.CreateProForm, _: schemas.CurrentUser = Depends(utils.get_current_user)):
    """创建项目数据库表"""
    try:
        tbname = req.proname + "_zones"
        await database.create_zones_tb(tbname)
    except:
        raise resource.CREATE_ZONES_ERROR
    return schemas.Response(
        message=f"创建{tbname}表成功!",
        code=200
    )


@router.get("/getpronames", response_model=schemas.ListResponse, name="zones_tb:show")
async def get_zones(_: schemas.CurrentUser = Depends(utils.get_current_user)):
    try:
        tbs = await database.select_zones_table()
        tbs = [value[0] for value in tbs]
    except:
        raise resource.SELECT_ZONES_ERROR
    return schemas.ListResponse(
        message="获取项目信息成功!",
        code=200,
        data=tbs
    )


@router.get("/zonelist", response_model=schemas.ListResponse, name="zones:list")
async def get_zone_list(pageNum, pageSize, tb, _: schemas.CurrentUser = Depends(utils.get_current_user)):
    zones = await database.get_zone_list(tb)
    return schemas.ListResponse(
        message="获取区服列表成功!",
        code=200,
        data=zones
    )


@router.post("/openzone", response_model=schemas.OpenZoneResponse, name="zone:open")
async def open_zone(req: schemas.OpenZoneForm, current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    # 区服信息入库
    tb = req.proname.split('_')[0] + "_zones"
    await database.insert_zone_record(req, tb)
    # 目标机器上创建进程所需的环境
    data = {"ip": req.ip, "name": req.proname, "serverid": req.serverid}
    conn = utils.get_conn(req.ip)
    conn.open_zone(data)
    # 接口操作记录
    await database.insert_record_to_db(current_user["username"], f"开服:{req.proname} : {req.serverid}")
    return schemas.OpenZoneResponse(
        message=f"开服: f{req.proname}_{req.serverid} 成功!",
        code=200
    )


@router.post("/zonecmd", response_model=schemas.ListDictResponse, name="zone:operate")
async def operate_zone(req: schemas.ZoneCmdForm , current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for zone in req.zones:
            zone["cmd"] = req.cmd
            future_conn = executor.submit(utils.get_conn, zone['server_ip']).result()
            data.append(future_conn.cmd_zone(zone))
            # 接口操作记录
            await database.insert_record_to_db(current_user["username"], f"{req.cmd}: {zone}")
    return schemas.ListDictResponse(
        message="zone cmd 成功!",
        code=200,
        data=data
    )


@router.get("/svnuphost", response_model=schemas.ListResponse, name="svn:update")
async def svn_update(tb: str, current_user: schemas.CurrentUser = Depends(utils.get_current_user)):
    ips = await database.select_server_ip(tb)
    # future_ret = utils.concurrent_rpc_svn(ips)
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ips)) as executor:
        future_conn = {executor.submit(utils.get_conn, ip[0]): ip for ip in ips}
        future_ret = [(future.result(timeout=600), future_conn[future][0]) for future in concurrent.futures.as_completed(future_conn)]
    data = [ (rcon[1], rcon[0].svn_up()) for rcon in future_ret ]
    # 接口操作记录
    await database.insert_record_to_db(current_user["username"], f"svn更新:{tb}")
    return schemas.ListResponse(
        message="获取项目ip成功!",
        code=200,
        data=data
    ) 


@router.get("/binupdate", name="bin:update")
async def bin_update(_: schemas.CurrentUser = Depends(utils.get_current_user)):
    pass
