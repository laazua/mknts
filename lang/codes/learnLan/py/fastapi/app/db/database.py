# -*- coding: utf-8 -*-
"""
数据库操作
"""

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import db_setting
from app.models import User


@contextmanager
def session_scope():
    try:
        engine = create_engine(db_setting.url)
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
        session.commit()
    except Exception as _:
        session.rollback()
        raise
    finally:
        session.close()


def query(username: str):
    with session_scope() as session:
        row = session.query(User).filter(User.username == username).first()
    return row


def query_user(username: str, password: str):
    with session_scope() as session:
        one = session.query(User).filter(User.username == username, User.password == password).first()
        if not one:
            return {}
        return {"username": one.username}


def add_user(username: str, password: str, role: str):
    new_user = User(username=username, password=password, role=role)
    with session_scope() as session:
        session.add(new_user)


def delete_user(username: str) -> bool:
    with session_scope() as session:
        row = session.query(User).filter(User.username == username).first()
        if row:
            session.delete(row)
            session.commit()
            return True
        else:
            return False


def change_password(username: str, password: str, new_password: str) -> bool:
    with session_scope() as session:
        # row = session.query(User).filter(User.username == username, User.password == password).\
        #    update({User.password: new_password})
        row = session.query(User).filter(User.username == username, User.password == password).first()
        row.password = new_password
        session.commit()
        if row:
            return True
        else:
            return False
