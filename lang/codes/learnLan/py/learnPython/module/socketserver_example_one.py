# -*- coding: utf-8 -*-
"""
socketserver 模块是一个创键网络服务器的框架.
它定义了通过 TCP，UDP，Unix 流和 Unix 数据报处理同步网络请求(服务器请求处理程序阻塞,直到请求完成)的类.
它还提供了混合类，可以轻松转换服务器，为每个请求使用单独的线程或进程.

服务器类型:
BaseServer类 ->> 定义了API,并不打算实例化和直接使用.
TCPServer类  ->> 使用TCP/IP套接字进行通信.
UDPServer类  ->> 使用数据包套接字进行通信.
UnixStreamServer和UnixDatagramServer ->> 使用Unix域套接字进行通信.
"""

import socketserver


class RequestHandler(socketserver.BaseRequestHandler):
    """请求处理类"""
    def __init__(self, request, client_address, server):
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        return socketserver.BaseRequestHandler().setup(self)

    def handle(self):
        """重写此方法,处理data"""
        while True:
            data = self.request.recv(1024)
        self.request.send(data)
        return

    def finish(self):
        return socketserver.BaseRequestHandler.finish(self)


class Server(socketserver.TCPServer, socketserver.ThreadingMixIn):
    def __init__(self, server_address, handler_class=RequestHandler,):
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        return socketserver.TCPserver.process_request(self, request, client_address)

    def server_close(self):
        return socketserver.TCPserver.server_close(self)

    def finish_request(self, request, client_address):
        return socketserver.TCPserver.finish_request(self, request, client_address)

    def shutdown(self):
        return socketserver.TCPserver.shutdown(self)


if __name__ == '__main__':
    import socket
    import threading

    address = ("0.0.0.0", 8888)
    server = Server(address, RequestHandler)
    ip, port = server.server_address
    print("server starting on {}:{}".format(ip, port))

    ## 在线程中启动
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()