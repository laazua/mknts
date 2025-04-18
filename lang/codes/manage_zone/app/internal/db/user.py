# @Time:        2022-08-04
# @Author:      Sseve
# @File:        user.py
# @Description: all user db operations

from . import MonDb


class UserDb(MonDb):
    def __init__(self) -> None:
        super(UserDb, self).__init__()

    @property
    def add(self):
        pass
