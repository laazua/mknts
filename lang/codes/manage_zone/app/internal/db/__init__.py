# @Time:        2022-08-04
# @Author:      Sseve
# @File:        __init__.py
# @Description: all db objects

from datetime import datetime
from config import settings
from mongoengine import connect, Document, StringField, \
     ListField, DateTimeField, IntField


class MonDb:
    def __init__(self) -> None:
        self._db = connect(host=f"{settings.db_address}")
    
    @property
    def get_ips(self) -> list:
        return [zone.ip for zone in Zone.objects]


# about document class, if field in class named id, 
# and mut pass parament primary_key=True to it
class User(Document):
    name      = StringField(min_length=2, max_length=120, required=True)
    password  = StringField(min_length=6, max_length=240, required=True)
    Roles     = ListField(required=True)
    date_time = DateTimeField(default=datetime.utcnow)


class Role(Document):
    name      = StringField(min_length=2, max_length=120, required=True)
    menus     = ListField(required=True)
    date_time = DateTimeField(default=datetime.utcnow)


class Menu(Document):
    name      = StringField(min_length=2, max_length=120, required=True)
    date_time = DateTimeField(default=datetime.utcnow)


class Zone(Document):
    ip        = StringField(required=True)
    name      = StringField(required=True)
    zone_id   = IntField(primary_key=True, required=True)
    date_time = DateTimeField(default=datetime.utcnow)
