# @Time:        2022-08-04
# @Author:      Sseve
# @File:        zone.py
# @Description: all zone db operations
from . import MonDb, Zone


class ZoneDb(MonDb):
    def __init__(self):
        super(ZoneDb, self).__init__()

    def add(self, zones) -> bool:
        try:
            _zones = [ Zone(zone_id=int(zone['id']), ip=zone['ip'], name=zone['name']) for zone in zones.zones ]
            _ = [ zone.save() for zone in _zones ]
            return True
        except Exception as e:
            print('add zone to db failed: ', e)
            return False

    def get(self) -> list:
        try:
            return [ {'ip': zone.ip, 'name': zone.name, 'zone_id': zone.zone_id} for zone in Zone.objects ]
        except Exception as e:
            print('get zone list failed: ', e)
            return None


zone_db = ZoneDb()
