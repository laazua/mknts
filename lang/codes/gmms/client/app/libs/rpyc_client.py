# -*- coding:utf-8 -*-
import os
import rpyc
import concurrent


path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
KEY_FILE = path + "/pem/ca.key"
CERT_FILE = path + "/pem/ca.cert"

class RpcClient:
    def __init__(self, ip, port, keyfile=KEY_FILE, certfile=CERT_FILE):
        self._ip = ip
        self._port = port
        self._keyfile = keyfile
        self._certfile = certfile
        self.bgsrv = rpyc.BgServingThread(self.conn)
        self.root = self.conn.root   # 数据格式字典的形式

    @property
    def conn(self):
        return rpyc.ssl_connect(self._ip, port=self._port, keyfile=self._keyfile, certfile=self._certfile)