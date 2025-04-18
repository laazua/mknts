# @Time:        2022-08-04
# @Author:      Sseve
# @File:        host.py
# @Description: all host db operations

from . import MonDb


class HostDb(MonDb):
    def __init__(self) -> None:
        super(HostDb, self).__init__()
        