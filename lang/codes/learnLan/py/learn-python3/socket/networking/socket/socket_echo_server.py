# -*-coding:utf-8-*-
"""
server && client mod
"""

import socket, sys


# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 地址绑定
server_address = ('127.0.0.1', 8888)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# 监听连接
sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from ', client_address)
        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(64)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to client')
                connection.sendall(data)
            else:
                print('no data from ', client_address)
                break
    finally:
        connection.close()
