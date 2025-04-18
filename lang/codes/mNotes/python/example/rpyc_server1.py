# -*- coding:utf-8 -*-
import rpyc
from rpyc.utils.authenticators import SSLAuthenticator
from rpyc.utils.server import ThreadedServer

class SlaveService(rpyc.Service):
    def on_connect(self, conn):
        return super().on_connect(conn)

    def on_disconnect(self, conn):
        return super().on_disconnect(conn)
    
    def exposed_mprint(self, data):
        print(data['aaa'])


auth = SSLAuthenticator("./ca.key", "./ca.cert")
server = ThreadedServer(SlaveService, port=8880, authenticator=auth)
server.start()