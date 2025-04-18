# @Time:        2022-08-04
# @Author:      Sseve
# @File:        user.py
# @Description: all user db operations
from . import MonDb, User
from internal.utils import hashed_pwd


class UserDb(MonDb):
    def __init__(self):
        super(UserDb, self).__init__()

    def add(self, user: User) -> bool:
        try:
            _user = User(
                name = user.name,
                password = hashed_pwd(user.pwd_one),
                roles = user.roles,
                desc = user.desc,
                avatar = user.avatar
            )
            _user.save()
            return True
        except Exception as e:
            print('add user failed: ', e)
            return False

    def delete(self, user: User) -> bool:
        try:
            _user = User.objects.get(name=user.name)
            _user.delete()
            _user.save()
            return True
        except Exception as e:
            print("delete user failed: ", e)
            return False

    def get(self) -> list:
        try:
            return [{'name': user.name, 'desc': user.desc, 'roles': user.roles, 'ctime': user.create_time, 'avatar': user.avatar} for user in User.objects]
        except Exception as e:
            print('get user failed: ', e)
            return None

    def check(self, name: str = None, user: User = None):
        if not name:
            return User.objects.get(name=user.username)
        else:
            return User.objects.get(name=name)


user_db = UserDb()