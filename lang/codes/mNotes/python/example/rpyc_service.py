import rpyc


class MyService(rpyc.Service):
    def on_connect(self, conn):
        return super().on_connect(conn)
    def on_disconnect(self, conn):
        return super().on_disconnect(conn)
    
    def exposed_foobar(self, remote_str):
        return {"foo":remote_str}


if __name__ == "__main__":
    server = rpyc.utils.server.ThreadedServer(MyService, port=8888)
    server.start()
    
