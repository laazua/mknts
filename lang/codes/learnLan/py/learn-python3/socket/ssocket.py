# -*- coding: utf-8 -*- 
"""
socket:
server function order: socket(), bind(), listen(), accept()[accept()可重复服务多个客户端]
                 note: sendall()/recv()在accept()返回的新套接字上发送.
client function order: socket(), connect()

"""

import socket
 