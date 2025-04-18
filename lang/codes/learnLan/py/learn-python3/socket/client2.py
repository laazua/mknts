# -*- coding: utf-8 -*-

"""
IPV4 && IPV6 support
echo client program
"""

import sys, socket

HOST = 'test.com'
PORT = 8889
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socketype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socketype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print("cant open socket")
    sys.exit(1)
with s:
    s.sendall(b"hello, world")
    data = s.recv(1024)
print("received", repr(data))