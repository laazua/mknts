# 测试 test_socketserver.py

import sys
import socket


data = " ".join(sys.argv[1:])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('0.0.0.0', 8888))
    sock.sendall(bytes(data + "\n", "utf-8"))
    recv_data = str(sock.recv(1024), "utf-8")


print(f"send: {data}")
print(f"recv: {recv_data}")