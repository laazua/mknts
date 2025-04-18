# -*- coding: utf-8 -*-
"""
数据库实例模型
"""
from sqlalchemy import (
    Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    # user table
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(128), unique=True)
    password = Column("password", String(256))
    role = Column("role", String(128))


class Role(Base):
    __tablename__ = "role"

    # role table
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), unique=True)
