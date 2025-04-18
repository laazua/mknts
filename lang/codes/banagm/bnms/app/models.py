# -*- coding: utf-8 -*-
# 数据库操作的表映射模型
import sqlalchemy
from app.database import metadata


# 系统用户表
bn_user = sqlalchemy.Table(
    'bn_user',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('username', sqlalchemy.String),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('rolename', sqlalchemy.String),
    sqlalchemy.Column('avatar', sqlalchemy.String),
    sqlalchemy.Column('introduction', sqlalchemy.String)
)


# # 游戏进程区服信息表
# mds_server = sqlalchemy.Table(
#     'mds_server',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
#     sqlalchemy.Column('alias', sqlalchemy.String),
#     sqlalchemy.Column('serverName', sqlalchemy.String),
#     sqlalchemy.Column('serverId', sqlalchemy.Integer),
#     sqlalchemy.Column('serverIp', sqlalchemy.String),
#     sqlalchemy.Column('gameDbUrl', sqlalchemy.String),
#     sqlalchemy.Column('gameDbPort', sqlalchemy.Integer),
#     sqlalchemy.Column('gameDbName', sqlalchemy.String),
# )

# 系统路由表 1
bn_menu = sqlalchemy.Table(
    'bn_menu',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('path', sqlalchemy.String),
    sqlalchemy.Column('component', sqlalchemy.String),
    sqlalchemy.Column('redirect', sqlalchemy.String),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('meta', sqlalchemy.String),
    sqlalchemy.Column('children', sqlalchemy.String)
)

# 系统路由表 2
bn_submenu= sqlalchemy.Table(
    'bn_submenu',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('path', sqlalchemy.String),
    sqlalchemy.Column('component', sqlalchemy.String),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('meta', sqlalchemy.String),
    sqlalchemy.Column('mu_fk', sqlalchemy.Integer)
)
