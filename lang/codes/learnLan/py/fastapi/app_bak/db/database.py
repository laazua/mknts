# -*- coding: utf-8 -*-
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://test:123456@127.0.0.1:3306/opms"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""
# pip install sqlalchemy
from sqlalchemy import  create_engine
# 初始化数据库连接，修改为你的数据库用户名和密码
engine = create_engine('mysql+mysqlconnector://user:password@host:port/DATABASE')

# 引用数据类型
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# 定义 User 对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表结构
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255))
    user_age = Column(Integer)


# 增删改查
from sqlalchemy.orm import sessionmaker
# 创建 DBSession 类型:
DBSession = sessionmaker(bind=engine)
# 创建 session 对象:
session = DBSession()

# 增:
new_user = User(user_id=100, user_name="Nan")
session.add(new_user)

# 删:
row = session.query(User).filter(User.user_name=="Nan").first()
session.delete(row)

# 改:
row = session.query(User).filter(User.user_name=="Nan").first()
row.user_age = 20

# 查
rows = session.query(User).filter(User.user_age >= 12).all()

# 提交保存到数据库
session.commit()

# 关闭session:
session.close()
