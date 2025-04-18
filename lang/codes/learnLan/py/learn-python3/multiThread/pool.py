# -*- coding: utf-8 -*-

"""
线程池:concurrent.futures
"""
from concurrent.futures import ThreadPoolExecutor
from socket import socket, SOCK_STREAM, AF_INET


# 第一个例子 ThreadPoolExecutor创建
def client(sk, addr):
    print('Connect from ', addr)
    while True:
        msg = sk.recv(1024)
        if not msg:
            break
        sk.sendall(msg)


def server(addr):
    pool = ThreadPoolExecutor(50)
    sk = socket(AF_INET, SOCK_STREAM)
    sk.bind(addr)
    sk.listen(5)
    while True:
        client_sk, client_addr = sk.accept()
        pool.submit(client, client_sk, client_addr)


# 第二个例子, queue
from threading import Thread, stack_size
from queue import Queue

#降低虚拟内存使用
stack_size(65536)

def echo_client(q):
    sk, addr = q.get()
    print("Connect from ", addr)
    while True:
        msg = sk.recv(1024)
        if not msg:
            break
        sk.sendall(msg)
    print("client closed connection")
    sk.close()


def echo_server(addr, nwrkers):
    q = Queue()
    for  i in range(nwrkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start

    sk = socket(AF_INET, SOCK_STREAM)
    sk.bind(addr)
    sk.listen(5)
    while True:
        client_sk, client_addr = sk.accept()
        q.put((client_sk, client_addr))


if __name__ == '__main__':
    server(('',2222))
    echo_server(("",3333), 20)