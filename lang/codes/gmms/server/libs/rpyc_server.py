# -*- coding:utf-8 -*-
import os
import re
import rpyc
from rpyc.utils.server import ThreadedServer
from rpyc.utils.authenticators import SSLAuthenticator
from libs import resource
from libs.daemon import Daemon
from libs.comm import Utils
from libs.config import sev_con


path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
KEY_FILE = path + "/pem/ca.key"
CERT_FILE = path + "/pem/ca.cert"


class RpcService(rpyc.Service, Utils):
    def on_connect(self, conn):
        return super().on_connect(conn)

    def on_disconnect(self, conn):
        return super().on_disconnect(conn)

    def exposed_open_zone(self, data):
        """开服"""
        gm_dir = f"/data/game/{data['name']}_{data['serverid']}"
        # 创建进程目录
        if not self._mk_dir(gm_dir):
            return resource.MSG_MK_DIR_ERROR
        # 拷贝配置文件
        if self._file_cp(sev_con.SVNDIR, gm_dir)[0]:
            return resource.MSG_CP_CONF_ERROR
        # 拷贝程序文件
        if self._file_cp(sev_con.BINSRC + "/gameserv-beta", gm_dir)[0]:
            return resource.MSG_CP_BIN_ERROR
        return resource.MSG_OPEN

    def exposed_cmd_zone(self, data):
        """start|stop|check"""
        gm_cmd = data["cmd"]
        gm_id = data["server_id"]
        gm_name = data["server_name"]
        gm_dir =sev_con.GM_PATH +  gm_name + '_' + str(gm_id)
        # 启动|关闭|检测游戏进程
        if gm_cmd in ["start", "stop", "check"]:
            cmd = f"cd {gm_dir} && sh {sev_con.GM_SCRIPT} {gm_cmd} 2>/dev/null"
            result = self._execute_cmd(cmd)
            if result[1]:
                return {"server_name": gm_name, "server_id": gm_id, "msg":result[1]}
            else:
                return {"server_name": gm_name, "server_id": gm_id, "msg":result[0]}
        elif gm_cmd == "upconf":
            if self._file_cp(sev_con.SVNDIR, gm_dir)[0]:
                return {"server_name": gm_name, "server_id": gm_id, "msg":"配置更新失败!"}
            return {"server_name": gm_name, "server_id": gm_id, "msg":"配置更新成功"}
        else:
            if self._file_cp(sev_con.BINSRC + "/gameserv-beta", gm_dir):
                return {"server_name": gm_name, "server_id": gm_id, "msg":"配置更新失败"}
            return {"server_name": gm_name, "server_id": gm_id, "msg":"bin更新成功"}

    def exposed_svn_up(self):
        """更新主机的svn配置"""
        if self._svn_up()[0]:
            return resource.SVN_UP_NO
        svn_info = self._svn_info()
        if not svn_info[0]:
            svn_ver = re.findall(r"最后修改的版本: (.*)", svn_info[1])
        return resource.SVN_UP_YES.format(svn_ver)

    def exposed_bin_up(self, data):
        """更新主机的bin文件"""
        pass


class Server(Daemon):
    def __init__(self, pidfile, stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
        super().__init__(pidfile, stdin=stdin, stdout=stdout, stderr=stderr)
    
    def run(self):
        auth = SSLAuthenticator(KEY_FILE, CERT_FILE) 
        # 配置protocol_config
        serve = ThreadedServer(
            RpcService(), 
            port=sev_con.RPCPORT, 
            authenticator=auth, 
            protocol_config={"allow_public_attrs": True, "allow_all_attrs": True})
        serve.start()