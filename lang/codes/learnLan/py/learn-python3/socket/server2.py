# -*- coding: utf-8 -*-

"""
IPV4 && IPV6 support
echo server program
"""

import sys, socket

HOST = None
PORT = 8888
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socketype, proto, canonname,sa = res
    try:
        s = socket.socket(af, socketype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(5)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('cant open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print("commected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)