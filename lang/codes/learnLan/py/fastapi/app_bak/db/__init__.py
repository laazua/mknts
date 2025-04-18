# -*- coding: utf-8 -*-
"""
数据库连接
engine = create_engine(url)
DBsession = sessionmaker(bind=engine)
dbsession = scoped_session(DBsession)  # 多线程
Base = declaratve_base()
md = MetaData(bind=engine)
"""
import time
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.setting import DBConfig
from .models import UserRoles, Users, Roles
from app.common import hash_password


@contextmanager
def session_scope():
    engine = create_engine(DBConfig.url)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as _:
        session.rollback()
        raise
    finally:
        session.close()


def query(username: str):
    try:
        with session_scope() as session:
            user = session.query(Users).filter_by(name=username).first()
            session.refresh(user)
            session.expunge(user)
        if user:
            return user
        else:
            return None
    except Exception as e:
        print("query:", e)
        return None
    

def insert(username: str, password: str, role: str):
    try:
        with session_scope() as session:
            session.add(Users(name=username, password=hash_password(password), role=role, status='on', ctime=time.strftime("%Y-%m-%d")))
            session.commit()
    except Exception as e:
        print("insert:", e)
        return None

def delete(username: str):
    user = query(username)
    if user:
        try:
            with session_scope() as session:
                session.delete(user)
                session.commit()
            return True
        except Exception as e:
            print("delete:", e)
            return False


# db_connect
def init_engine():
    return create_engine(DBConfig.url, poolclass=None, pool_size=5,
                         max_overflow=20, pool_recycle=3600, pool_pre_ping=True)


class DBContext:
    def __init__(self):
        self.__engine = self.__get_db_engine()

    @staticmethod
    def __get_db_engine():
        return init_engine()

    @property
    def session(self):
        self.__session

    def __enter__(self):
        self.__session = sessionmaker(bind=self.__engine)()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__session.rollback()
        else:
            self.__session.commit()
        self.__session.close()

    def get_session(self):
        return self.__session
