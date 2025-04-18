# -*- coding: utf-8 -*-
"""
a simple example.
"""

import socketserver


class MyRequestHandler(socketserver.StreamRequestHandler):
    """
    处理请求类,继承StreamRequestHandler
    重写handle方法
    """
    def handle(self):
        while True:
            pass


class Server(socketserver.TCPServer, socketserver.ThreadingMixIn):
    """
    多线程处理请求服务,
    socketserver封装了ThreadingTCPServer可以直接使用替代Server
    """
    pass


if __name__ == '__main__':
    address = ("127.0.0.1", 8080)
    # serve = socketserver.ThreadingTCPServer(address, MyRequestHandler)
    serve = Server(address, MyRequestHandler)
    ip, port = serve.server_address
    print("server starting on {}:{}".format(ip, port))