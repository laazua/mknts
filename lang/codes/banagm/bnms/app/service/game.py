# -*- coding: utf-8 -*-
import os
import time
from app.database import db
from app.database import create_zone
from app.common import send_data
from app.config import cnf


async def result_zone_list(req):
    sql = f"SELECT COUNT(*) FROM {req.tb};"
    if not req.tb:
        return {'code': 201, 'data': {'total': 0, 'zones': None }, 'message': 'get none zone'}
    num = await db.fetch_one(query=sql)
    offset_data = req.size * (req.num - 1)
    sql = f"SELECT alias, serverName,serverId,serverIp FROM {req.tb} LIMIT {req.size} OFFSET {offset_data}"
    # sql = mds_server.select().offset(offset_data).limit(req.size)
    zone_query = await db.fetch_all(query=sql)
    print(zone_query)
    data = []
    for zone_q in zone_query:
        zone = {}
        zone['alias'], zone['serverName'], zone['serverId'], zone['serverIp'] = zone_q
        data.append(zone)
    return {'code': 200, 'data': {'total': num[0], 'zones': data }, 'message': 'get zone list success.'}


async def result_new_pro(req):
    sql = f"CREATE TABLE IF NOT EXISTS `{req.proName}` ( \
            `id` INT UNSIGNED AUTO_INCREMENT, `alias` VARCHAR(64), `serverName` VARCHAR(64), \
            `serverId` INT, `serverIp` VARCHAR(128), `gameDbUrl` VARCHAR(128), \
            `gameDbPort` INT, `gameDbName` VARCHAR(64), PRIMARY KEY (`id`) \
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    try:
        await db.execute(query=sql)
        return {'code': 200, 'data': None, 'message': '创建成功!'}
    except:
        return {'code': 201, 'data': None, 'message': '创建失败!'} 
    

async def result_get_pro():
    sql = "SHOW TABLES LIKE 'bn_mds_%';"
    table_query = await db.fetch_all(query=sql)
    project_name = []
    for item in table_query:
        project_name.append(item[0])
    return {'code': 200, 'data': project_name, 'message': 'ok'}


async def result_open_serve(req):
    zone_info = {}
    zone_info['cmd'] = 'open'
    zone_info['serverName'] = req.serverName
    zone_info['serverId'] = req.serverId
    zone_info['serverIp'] = req.serverIp
    zone_info['retStatus'] = '开服成功!'
    zone_insert = await create_zone(req)
    if not zone_insert:
        return {'code': 201, 'data': None, 'message': '区服信息插入数据库失败'}
    socket_send_data = []
    socket_send_data.append(zone_info)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': '开服成功!'}


async def result_svn_update(tb, cmd):
    """主机本地svn更新"""
    tb_query = f"SELECT DISTINCT serverIp FROM {tb}"
    tb_result = await db.fetch_all(query=tb_query)
    socket_send_data = []
    for ip in tb_result:
        data = {'serverIp': ip[0], 'cmd': cmd}
        socket_send_data.append(data)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': 'svn更新成功!'}


async def result_bin_host(tb, cmd):
    tb_query = f"SELECT DISTINCT serverIp FROM {tb}"
    tb_result = await db.fetch_all(query=tb_query)
    socket_send_data = []
    for ip in tb_result:
        data = {'serverIp': ip[0], 'cmd': cmd}
        socket_send_data.append(data)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': 'bin更新成功!'}


async def result_bin_list():
    files = []
    print(os.listdir(cnf.bin_path))
    for file in os.listdir(cnf.bin_path):
        file_info = {}
        if not file.startswith('game'): continue
        fliemt = time.localtime(os.stat(cnf.bin_path + '/' + file).st_ctime)
        fileCtime = time.strftime("%Y-%m-%d %H:%M:%S", fliemt)
        file_info['fileName'] = file
        file_info['fileCtime'] = fileCtime
        files.append(file_info)
    return {'code': 200, 'data':files, 'message': 'bin列表文件获取成功'}


async def result_con_update(zones):
    socket_send_data = []
    for zone in zones:
        for item in zone[1]:
            item['cmd'] = 'update'
            socket_send_data.append(item)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': '配置文件更新成功!'}


async def result_zone_start(zones):
    socket_send_data = []
    for zone in zones:
        for item in zone[1]:
            item['cmd'] = 'start'
            socket_send_data.append(item)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': '区服启动成功!'}


async def result_zone_stop(zones):
    socket_send_data = []
    for zone in zones:
        for item in zone[1]:
            item['cmd'] = 'stop'
            socket_send_data.append(item)
    socket_recv_data = await send_data(socket_send_data)
    return {'code': 200, 'data': socket_recv_data, 'message': '区服关闭成功!'}


async def result_zone_check(zones):
    socket_send_data = []
    for zone in zones:
        for item in zone[1]:
            item['cmd'] = 'check'
            socket_send_data.append(item)
    socket_recv_data = await send_data(socket_send_data)
    print('socket_recv_data: ', socket_recv_data)
    return {'code': 200, 'data': socket_recv_data, 'message': '区服检查成功!'}


async def result_bin_update(zones):
    socket_send_data = []
    for zone in zones:
        for item in zone[1]:
            item['cmd'] = 'binupdate'
            socket_send_data.append(item)
    socket_recv_data = await send_data(socket_send_data)
    print('socket_recv_data: ', socket_recv_data)
    return {'code': 200, 'data': socket_recv_data, 'message': 'bin更新成功!'}


async def result_host_status(tb, cmd):
    tb_query = f"SELECT DISTINCT serverIp FROM {tb}"
    tb_result = await db.fetch_all(query=tb_query)
    socket_send_data = []
    for ip in tb_result:
        data = {'serverIp': ip[0], 'cmd': cmd}
        socket_send_data.append(data)
    socket_recv_data = await send_data(socket_send_data)
    print(socket_recv_data)
    return {'code': 200, 'data': socket_recv_data, 'message': 'svn更新成功!'}
