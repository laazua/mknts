import os
from app.config import cfg
from app.internal.grpc.zone import zone_pb2


def add_zone(zone: zone_pb2.ZoneReq) -> str:
    zone_path = f"{cfg.get('zone', 'path')}/{zone.zname}_{zone.zid}"
    if not os.path.exists(zone_path):
        os.makedirs(zone_path)
    print("正在开服...")

    return f"{zone.zname}_{zone.zid}开服成功"


def upt_conf(zone: zone_pb2.ZoneReq) -> str:
    zone_path = f"{cfg.get('zone', 'path')}/{zone.zname}_{zone.zid}"
    print(zone_path)

    return f"{zone.zname}_{zone.zid}配置更新成功"


def upt_bin(zone: zone_pb2.ZoneReq) -> str:
    zone_path = f"{cfg.get('zone', 'path')}/{zone.zname}_{zone.zid}"
    print(zone_path)

    return f"{zone.zname}_{zone.zid}程序更新成功"


def zone_opt(zone: zone_pb2.ZoneReq) -> str:
    zone_path = f"{cfg.get('zone', 'path')}/{zone.zname}_{zone.zid}"
    print(zone_path)

    return f"{zone.zname}_{zone.zid}{zone['target']}成功"
