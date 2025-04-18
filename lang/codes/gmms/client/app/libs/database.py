# -*- coding:utf-8 -*-
import datetime
import databases
from app.libs.config import AppCon
from app.libs import utils, resource


db = databases.Database(AppCon.db_url)


async def get_user_by_name(username):
    return await db.fetch_one(query=resource.GET_USER_BY_NAME.format(username))


async def insert_user_to_db(username, password):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = [
        {
            "username": username, 
            "password": utils.encode_password(password), 
            "create_at": current_time, 
            "update_at": current_time
        }, 
    ]
    await db.execute_many(query=resource.INSERT_USER_TO_DB, values=values)
    

async def create_zones_tb(tbname):
    await db.execute(query=resource.CREATE_ZONES_TB.format(tbname))


async def select_all_users():
    users_row = await db.fetch_all(query=resource.SELECT_ALL_USERS)
    data = []
    for index, value in enumerate(users_row):
        data.append({"index": index + 1, "username": value[0]})
    return data

async def delete_user(username):
    await db.execute(query=resource.DELETE_ONE_USER.format(username))


async def insert_record_to_db(username, option):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_time = datetime.datetime.now().strftime("%Y-%m-%d")
    values = [
        {
            "username": username,
            "opt": option,
            "create_at": current_time,
            "day_time": day_time
        },
    ]
    await db.execute_many(query=resource.INSERT_USER_LOG, values=values)


async def select_user_record(usernmae, datetime):
    return await db.fetch_all(resource.SELECT_USER_LOG.format(usernmae, datetime))


async def select_zones_table():
    return await db.fetch_all(resource.SELECT_ZONES_TB)


async def select_server_ip(tb):
    return await db.fetch_all(resource.SELECT_SERVE_IP.format(tb))


async def insert_zone_record(zoneinfo, tb):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = [
        {
            "server_name": zoneinfo.proname,
            "server_id": zoneinfo.serverid,
            "server_ip": zoneinfo.ip,
            "create_at": current_time,
            "update_at": current_time,
            "is_combined": 0
        }
    ]
    await db.execute_many(query=resource.INSERT_ZONE_INFO.format(tb), values=values)


async def get_zone_list(tb):
    return await db.fetch_all(query=resource.GET_ZONE_LIST.format(tb))