# -*-coding:utf-8-*-

import sys, socket


# 创建TCP/IP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到server端监听的地址
server_address = ('127.0.0.1', 8888)
print('connection to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # 发送数据
    message = b'this is message, it will be repeated'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()