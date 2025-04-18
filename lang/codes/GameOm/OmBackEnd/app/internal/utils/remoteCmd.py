from fabric import Connection
from multiprocessing import Pool

from config import settings
from internal.utils.cmd import add_cmd, con_cmd, opt_cmd, node_cmd


def _run_cmd(zone, cmd):
    try:
        return {'name': zone['name'], 'id': zone['id'], 'msg': Connection(zone['ip']).run(cmd).stdout}
    except Exception as e:
        return {'name': zone['name'], 'id': zone['id'], 'msg': e}


def _zone_add(zone):
    """开服"""
    cmd = add_cmd.format(settings.gm_path + zone['name'] + '_' + str(zone['id']), 
        settings.gm_path + zone['name'] + '_' + str(zone['id']),
        settings.svn_user, settings.svn_password, settings.svn_address,
        settings.gm_path + zone['name'] + '_' + str(zone['id']))
    return _run_cmd(zone, cmd)
    

def _zone_bin(zone):
    """更新程序文件"""
    try:
        Connection(zone['ip']).put(settings.local_bin, settings.gm_path + zone['name'] + '_' + str(zone['id']))
        return {'name': zone['name'], 'id': zone['id'], 'msg': 'upload binfile success'}
    except Exception as e:
        return {'name': zone['name'], 'id': zone['id'], 'msg': e}


def _zone_con(zone):
    """更新配置"""
    cmd = con_cmd.format(settings.svn_user, settings.svn_password,
        settings.gm_path + zone['name'] + '_' + str(zone['id']))
    return _run_cmd(zone, cmd)


def _zone_start(zone):
    """启动区服"""
    cmd = opt_cmd.format(settings.gm_path + zone['name'] + '_' + str(zone['id']), settings.gm_shell, 'start')
    return _run_cmd(zone, cmd)


def _zone_stop(zone):
    """关闭区服"""
    cmd = opt_cmd.format(settings.gm_path + zone['name'] + '_' + str(zone['id']), settings.gm_shell, 'stop')
    return _run_cmd(zone, cmd)


def _zone_check(zone):
    """检查区服"""
    cmd = opt_cmd.format(settings.gm_path + zone['name'] + '_' + str(zone['id']), settings.gm_shell, 'check')
    return _run_cmd(zone, cmd)


def hand_zone(zones):
    """区服处理"""
    pool = Pool(settings.pools)
    results = []
    for z in zones.zones:
        if zones.target == "open":
            results.append(pool.apply_async(_zone_add, (z,)))
        if zones.target == "binfile":
            results.append(pool.apply_async(_zone_bin, (z,)))
        if zones.target == "config":
            results.append(pool.apply_async(_zone_con, (z,)))
        if zones.target == "start":
            results.append(pool.apply_async(_zone_start, (z,)))
        if zones.target == "stop":
            results.append(pool.apply_async(_zone_stop, (z,)))
        if zones.target == "check":
            results.append(pool.apply_async(_zone_check, (z,)))
    pool.close()
    pool.join()
    return [ r.get() for r in results ]   


def _host_msg(ip):
    """获取主机资源信息"""
    if not ip:
        return None
    else:
        try:
            return {'ip': ip, 'node': eval(Connection(ip).run(node_cmd.format(settings.nd_path)).stdout)}
        except Exception as e:
            return None


def hand_host(ips):
    """主机处理"""
    results = []
    pool = Pool(settings.pools)
    for ip in ips:
        results.append(pool.apply_async(_host_msg, (ip,)))
    pool.close()
    pool.join()
    return [ r.get() for r in results ]
