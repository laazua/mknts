# -*- coding: utf-8 -*-
"""
定义一些依赖工具函数
"""

from fastapi.requests import Request
from app.config import setting


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from app.config import db_setting


engine = create_engine(db_setting.url)
Base = declarative_base()


def get_db():
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session()
    try:
        return db
    except Exception as _:
        db.close()


def allow_ip(request: Request):

    if request.client.host not in setting.iplist:
        return False
    else:
        return True
