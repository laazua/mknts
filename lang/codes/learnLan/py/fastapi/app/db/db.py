# -*- coding: utf-8 -*
"""
db operation
"""

from app.models import User
from app.dependencies.utils import get_db


def create_user(username: str, password: str, db=get_db()):
    to_create = User(
        username=username,
        password=password
    )
    db.add(to_create)
    db.commit()


def query_user(username: str, password: str, db=get_db()):
    to_query = db.query(User).filter(User.username == username, User.password == password).first()
    if not to_query:
        return {}
    return {"username": to_query.username}


def delete_user(username: str, password: str, db=get_db()):
    db.query(User).filter(User.username == username, User.password == password).delete()
    db.commit()
    return True
