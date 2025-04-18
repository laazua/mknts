import os
import typing
from fabric import Connection
from app.grpc.zone import zone_pb2
from app import AppConfig, AppLogger


def create_zone_msg(zone: zone_pb2.ZoneRequest) -> typing.Tuple[str|typing.Any]:
    zonepath = "{0}/{1}_{2}".format(
        AppConfig.get("zone", "path"),
        zone.name,
        zone.number,
    )
    if not os.path.exists(zonepath):
        os.makedirs(zonepath)
    conn =  Connection(
                host=AppConfig.get("zone", "binIp"),
                user=AppConfig.get("ssh", "username"),
                connect_kwargs=dict(
                    password=AppConfig.get("ssh", "password")))
    return zonepath, conn


def upt_bin(zone: zone_pb2.ZoneRequest) -> str:
    zonepath, conn = create_zone_msg(zone)
    if not os.path.exists(zonepath):
        return "未开此服"
    #上传后端文件
    try:
       conn.get(AppConfig.get("zone", "binPath"),f"{zonepath}/gameserv")
    except Exception as e:
        return "上传后端文件失败"
    # 校验后端文件文件
    result = conn.local(f"md5sum {zonepath}/gameserv")
    upt_bin_result = f"后端文件更新成功: {result.stdout}"
    if not result.ok:
        AppLogger.error(f"{zonepath} 后端文件更新失败")
        return "后端文件更新失败"
    AppLogger.info(f"{zonepath} 后端文件更新成功")
    return upt_bin_result
    

def upt_con(zone: zone_pb2.ZoneRequest) -> str:
    zonepath, conn = create_zone_msg(zone)
    if not os.path.exists(zonepath):
        return "未开此服"
    if not zone.svnversion:
        AppLogger.error("未输入svn版本号")
        return "未输入svn版本号"
    # 更新配置
    svn_up = "svn --username {0} --password {1} up -r {2} {3}".format(
        AppConfig.get("svn", "username"),
        AppConfig.get("svn", "password"),
        zone.svnversion, zonepath)
    try:
        conn.local(svn_up)
        result = conn.local(f"svn info {zonepath}|grep Revision")
    except Exception as e:
        AppLogger.error(f"配置文件更新失败: {e}")
        return "配置文件更新失败"
    upt_con_result = f"配置文件更新成功: {result.stdout}"
    if not result.ok:
        AppLogger.error(f"{zonepath} 配置文件更新失败")
        return "配置文件更新失败"
    return upt_con_result

def add_zone(zone: zone_pb2.ZoneRequest) -> str:
    """
    返回的字符串中不能出现格式化的形式,否则报错:
    grpc._channel._InactiveRpcError
    """
    zonepath, conn = create_zone_msg(zone)
    if not os.path.exists(zonepath):
        return "未建进程目录"
    svn_co = "svn --username {0} --password {1} co {2} -r {3} -q {4}".format(
        AppConfig.get("svn", "username"),
        AppConfig.get("svn", "password"),
        AppConfig.get("svn", "repoUrl"),
        zone.svnversion, zonepath)
    try:
        conn.local(svn_co)
        result = conn.local(f"svn info {zonepath}|grep Revision")
    except Exception as e:
        AppLogger.error(f"导出配置文件失败: {e}")
        return "导出配置文件失败"
    add_zone_result = f"开服成功: {result.stdout}"
    if not result.ok:
        AppLogger.error(f"{zonepath} 导出配置文件失败")
        return "导出配置文件失败"
    return add_zone_result


def opt_zone(zone: zone_pb2.ZoneRequest) -> str:
    zonepath, conn = create_zone_msg(zone)
    opt_cmd = f"cd {zonepath} && bash {AppConfig.get('zone', 'shell')} {zone.target}"
    try:
        result = conn.local(opt_cmd)
    except Exception as e:
        AppLogger.error(f"{zone.target}后端进程失败: {e}")
        return "操作后端进程失败"
    opt_zone_result = f"操作后端进程: {result.stdout}"
    if result.status != 0:
        return "操作后端进程失败"
    return opt_zone_result
