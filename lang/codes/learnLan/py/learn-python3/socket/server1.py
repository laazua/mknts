# -*- coding: utf-8 -*-

"""
IPV4
server endport: echo server program
"""

import socket

HOST = ''
PORT = 8888
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.bind((HOST, PORT))
        sk.listen(5)
        conn, addr = sk.accept()
        with conn:
            print("client addr: ", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
