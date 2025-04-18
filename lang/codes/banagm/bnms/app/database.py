# -*- coding: utf-8 -*-
# 数据库相关的操作

import databases
import sqlalchemy
from app.config import cnf


# databases db
db = databases.Database(cnf.db_url)


# sqlalchemy db 
# engine = sqlalchemy.create_engine(
#     cnf.db_url
# )
# SessionLocal = sqlalchemy.orm.sessionmaker(
#     bind=engine,
#     autocommit=False,
#     autoflush=False
# )
# Base = sqlalchemy.ext.declarative.declarative_base()
metadata = sqlalchemy.MetaData()
# metadata.create_all(engine)
# Base.metadata.create_all(engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def create_zone(req):
    try:
        sql = f"INSERT INTO {req.tb}(alias,serverName,serverId,serverIp,gameDbUrl,gameDbPort,gameDbName)VALUES(\
            :alias, :serverName, :serverId, :serverIp, :gameDbUrl, :gameDbPort, :gameDbName)"
        alias = req.tb.split('_')[-1]
        values = [
            {"alias": alias, "serverName": req.serverName, "serverId": int(req.serverId), "serverIp": req.serverIp,
             "gameDbUrl": req.serverIp, "gameDbPort": 3306, "gameDbName": "test"
            }
        ]
        await db.execute_many(query=sql, values=values)
        return True
    except:
        return False