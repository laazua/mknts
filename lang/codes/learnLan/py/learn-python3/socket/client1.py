# -*- coding: utf-8 -*-

"""
IPV4
client endport: echo client program
"""
import socket


HOST = ''
PORT = 8888
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
    sk.connect((HOST, PORT))
    sk.sendall(b'hahahaha')
    data = sk.recv(1024)
print('server mgs: ', repr(data))