# -*- coding: utf-8 -*-
"""
创建表
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData, engine, DateTime

Base = declarative_base()
db = ""
md = MetaData(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    createTime = Column(DateTime(''))
    passwrd_hashed = Column(String(128))



class Article(Base):
    """
    增删改查
    """
    __table__ = Table('article', md, autoload=True)