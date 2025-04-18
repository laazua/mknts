# -*- coding: utf-8 -*-

from fastapi import HTTPException, status
from app.database import db
from app.common import Token
from app.common import PwHash
from app.models import bn_menu
from app.models import bn_submenu


async def result_user_login(req):
    sql = f"SELECT username,password,rolename FROM bn_user WHERE username='{req.username}'"
    user = await db.fetch_one(query=sql)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='user not exists!')
    if not PwHash.verify_password(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='invalid password!')
    token = Token.create_token(data={'username': user.username, 'rolename': user.rolename})
    return {'code': 200, 'token': token, 'token_type': 'bearer'}


async def result_user_info(req):
    sql = f"SELECT * FROM bn_user WHERE username='{req.username}'"
    user = await db.fetch_one(query=sql)
    data = {}
    _, data['name'], _, data['role'], data['avatar'], _ = user
    return {'code': 200, 'data': data, 'msg': 'get user info success.'}


async def result_user_register(req):
    sql = f"SELECT username FROM bn_user WHERE username='{req.username}'"
    user = await db.fetch_one(query=sql)
    if user:
        return {'code': 201, 'data': None, 'msg': f"{user.username} register error!"}
    sql = f"INSERT INTO `bn_user` (`username`,`password`,`rolename`,`avatar`,`introduction`) VALUES \
        ('{req.username}','{PwHash.encode_password(req.password)}','{req.rolename}','{req.avatar}','{req.introduction}')"
    execute_result = await db.execute(sql)
    if not execute_result:
        return {'code': 201, 'data': None, 'msg': f"{user.username} register error!"}
    return {'code': 200, 'data': None, 'msg': f"{req.username} register success!"}


async def result_router_info():
    menu_query = bn_menu.select()
    submenu_query = bn_submenu.select()
    menu_query = await db.fetch_all(query=menu_query)
    submenu_query = await db.fetch_all(query=submenu_query)
    data = []
    for menu_q in menu_query:
        menu = {}
        menu_router = []
        for submenu_q in submenu_query:
            submenu = {}
            if menu_q.id == submenu_q.mu_fk:
                menu['id'] = menu_q.id
                menu['name'] = menu_q.name
                menu['path'] = menu_q.path
                menu['component'] = menu_q.component
                menu['redirect'] = menu_q.redirect
                menu['meta'] = menu_q.meta
                submenu['id'] = submenu_q.id
                submenu['path'] = submenu_q.path
                submenu['component'] = submenu_q.component
                submenu['name'] = submenu_q.name
                submenu['meta'] = submenu_q.meta
                menu_router.append(submenu)
                menu['children'] = menu_router
        data.append(menu)
    return {'code': 200, 'data': data, 'msg': 'get router success!'}
