# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    # 用户表
    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), unique=True)
    password = Column('password', String(256))
    role = Column('role', String(128))
    status = Column('status', String('10'), default='0')
    ctime = Column('ctime', DateTime(), default=datetime.now)

    def __repr__(self):
        return "username:{}, password: {}".format(self.name, self.password)


class Roles(Base):
    __tablename__ = 'roles'

    # 角色表
    role_id = Column('role_id', Integer, primary_key=True, autoincrement=True)
    role_name = Column('role_name', String(128), index=True)
    status = Column('status', String(5), default='0')
    ctime = Column('ctime', DateTime(), default=datetime.now, onupdate=datetime.now)


class UserRoles(Base):
    __tablename__ = 'user_roles'

    # 用户角色关联表
    user_role_id = Column('user_role_id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', String(11), index=True)
    user_id = Column('user_id', String(11), index=True)
    status = Column('status', String(5), default='0')
    utime = Column('utime', DateTime(), default=datetime.now, onupdate=datetime.now)
    ctime = Column('ctime', DateTime(), default=datetime.now)
