# -*-coding:utf-8-*-
"""
I/O 多路服用抽象
selectors 模块在select中平台特定的I/O监视函数之上提供了一个平台独立的抽象层.
selectors 中的API是基于事件的,与select中poll()类似,它有多个实现,并且这个模块会自动设置别名DefaultSelector来指示对当前系统配置为最
高效的一个实现
"""

import selectors
import socket


my_selector = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    """
    Callback for read events
    :param connection:
    :return:
    """
    global keep_running

    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # A readable client socket has data
        print(' received {!r}'.format(data))
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection
        print(' closing')
        my_selector.unregister(connection)
        connection.close()
        # Tell the main loop to stop
        keep_running = False


def accept(sock, mask):
    """
    callback for new connection
    :param sock:
    :return:
    """
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    my_selector.register(new_connection, selectors.EVENT_READ, read)


server_address = ('127.0.0.1', 8888)
print('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

my_selector.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('waiting for I/O')
    for key, mask in my_selector.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)

print('shutting down')
my_selector.close()
