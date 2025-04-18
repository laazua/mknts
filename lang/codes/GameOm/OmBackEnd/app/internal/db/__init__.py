# @Time:        2022-08-04
# @Author:      Sseve
# @File:        __init__.py
# @Description: all db objects

from datetime import datetime
from config import settings
from mongoengine import connect, Document, \
     StringField, ListField, IntField


class MonDb:
    def __init__(self) -> None:
        self._db = connect(host=f"{settings.db_address}")


# about document class, if field in class named id, 
# and mut pass parament primary_key=True to it
class User(Document):
    name        = StringField(min_length=2, max_length=120)
    password    = StringField(min_length=6, max_length=240)
    desc        = StringField()
    roles       = ListField()
    avatar      = StringField()
    create_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Zone(Document):
    ip          = StringField(required=True)
    name        = StringField(required=True)
    zone_id     = IntField(primary_key=True, required=True)
    create_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Log(Document):
    name        = StringField(required=True)
    action      = StringField(required=True)
    create_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
