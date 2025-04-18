from datetime import datetime
from tkinter.tix import Tree
from typing import Any
from mongoengine import connect, Document, \
    StringField, ListField
from internal.utils import config
from internal.utils.passwd import PasswdHandle


class User(Document):
    name        = StringField(min_length=2, max_length=120)
    password    = StringField(min_length=6, max_length=240)
    desc        = StringField(min_length=2, max_length=120)
    roles       = ListField()
    avatar      = StringField(min_length=2, max_length=240, default="xxxxxxxxx")
    create_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class UserDb:
    def __init__(self, user: dict = None, name: str = None)-> None:
        self.db = connect(host=config.DB_ADDRESS)
        self.user = user
        self.name = name

    @property
    def add(self) -> bool:
        try:
            user = User(
                name     = self.user["name"],
                password = PasswdHandle(plain_pwd=self.user["pwd_one"]).hash,
                roles    = self.user["roles"],
                desc     = self.user["desc"],
                avatar   = self.user["avatar"]
            )
            user.save()
            return True
        except Exception as e:
            print("add user to db failed: ", e)
            return False

    @property
    def delete(self) -> bool:
        try:
            user = User.objects.get(name=self.user["name"])
            user.delete()
            user.save()
            return Tree
        except Exception as e:
            print("delete user to db failed: ", e)
            return False

    @property
    def get(self) -> Any:
        try:
            user = [{"name": user.name, "desc": user.desc, "roles": user.roles, "ctime": user.create_time, "avatar": user.avatar} for user in User.objects]
            return user
        except Exception as e:
            print("get user failed: ", e)
            return None

    @property
    def check(self) -> Any:
        if not self.name:
            return User.objects.get(name=self.user["name"])
        return User.objects.get(name=self.name)
