# -*-coding:utf-8-*-
import socket
import sys


def get_constants(prefix):
    """
     创建一个字典,映射套接字模块和常量名称
    """
    return {
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }


families = get_constants('AF_')
types = get_constants('SOCK_')
protocaols = get_constants('IPPROTO_')

# 创建tcp/ip socket
sock = socket.create_connection(('127.0.0.1', 8888))
print('Family       :', families[sock.family])
print('Typpe        ', types[sock.type])
print('Protocol     :', protocaols[sock.proto])

try:
    message = b'this is the message, it will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_recevied = 0
    amount_expected = len(message)
    while amount_recevied < amount_expected:
        data = sock.recv(64)
        amount_recevied += len(data)
        print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()