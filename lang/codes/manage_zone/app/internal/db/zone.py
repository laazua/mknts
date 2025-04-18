# @Time:        2022-08-04
# @Author:      Sseve
# @File:        zone.py
# @Description: all zone db operations

from . import Zone
from . import MonDb


class ZoneDb(MonDb):
    def __init__(self, zones=None) -> None:
        super(ZoneDb, self).__init__()
        self._zones = zones

    @property
    async def add(self) -> bool:
        try:
            zones = [Zone(id=zone['zone_id'], ip=zone['ip'], name=zone['name']) for zone in self._zones]
            _ = [zone.save() for zone in zones]
            return True
        except Exception as e:
            print("add zone to db error: ", e)
            return False

    @property
    async def get(self) -> list:
        pass
