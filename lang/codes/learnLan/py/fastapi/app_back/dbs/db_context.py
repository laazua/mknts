# -*- coding: utf-8 -*-
"""
数据库连接
engine = create_engine(url)
DBsession = sessionmaker(bind=engine)
dbsession = scoped_session(DBsession)  # 多线程
Base = declaratve_base()
md = MetaData(bind=engine)
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.config import cfg


class DBContext:
    def __init__(self):
        self.__engine = self.__get_engine()

    @staticmethod
    def __get_engine():
        url = cfg.get_config('db')
        return create_engine(url.get('url'), poolclass=NullPool)

    @property
    def session(self):
        return self.__session

    def __enter__(self):
        self.__session = sessionmaker(bin=self.__engine)
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__session.rollback()
        else:
            self.__session.commit()
        self.__session.close()
