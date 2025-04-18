# @Time:        2022-08-04
# @Author:      Sseve
# @File:        host.py
# @Description: all host db operations

from . import MonDb, Zone


class HostDb(MonDb):
    def __init__(self) -> None:
        super(HostDb, self).__init__()

    def get_ips(self) -> list:
        return [ zone.ip for zone in Zone.objects ]


host_db = HostDb()
