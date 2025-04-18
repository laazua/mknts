# -*- coding: utf-8 -*-

"""
socketserver模块:
    socketserver.TCPServer:
    socketserver.UnixStreamServer
    socketserver.UDPServer:
    socketserver.UnixDatagramServer
    以上4个类用于实例化一个服务器类

详细操作参考官方文档.
"""

import socketserver

class TestServer(socketserver.BaseRequestHandler):
    """
    请求处理类
    """

    def handle(self):
        """
        处理请求,重写父类的handle方法
        """
        pass


if __name__ == "__main__":
    server_addr = ('127.0.0.1', 8888)
    print(serverAddr)

    # 实例化一个服务器类
    s = socketserver.TCPServer(server_addr, TestServer)
    
    # 根据实例化对象s进行操作.
