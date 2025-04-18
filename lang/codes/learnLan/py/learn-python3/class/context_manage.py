# -*- coding: utf-8 -*-
"""
让对象支持上下文管理,在类中实现enter()和exit()方法
更多上下文管理,参考contextmanager模块
"""

from socket import socket, AF_INET, SOCK_STREAM


class ContextManage:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()
