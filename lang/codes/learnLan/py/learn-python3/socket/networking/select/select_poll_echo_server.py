# -*-coding:utf-8-*-
import select
import socket
import sys
import queue


# create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# bind the socket to the part
server_address = ('127.0.0.1', 8888)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# listen for incoming connections
server.listen(5)

# keep up with the queues of outgoing messages.
message_queues = {}

# poll()超时值用毫秒表示,不是秒.
TIMEOUT = 1000

# poll()的事件标志:
# POLLIN        输入准备就绪
# POLLPRI       优先级输入准备就绪
# POLLOUT       能够接收输出
# POLLERR       错误
# POKKHUP       通道关闭
# POLLNVAL      通道为打开

# commonly used flag sets
READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT

# set up the poller
poller = select.poll()
poller.register(server, READ_ONLY)

# map file descriptors to socket objects.
fd_to_socket = {
    server.fileno(): server,
}

while True:
    # wait for at least one of the sockets to be ready for processing
    print('waiting for the next event', file=sys.stderr)
    events = poller.poll(TIMEOUT)
    for fd, flag in events:
        # retrieve the actual socket from its file descriptor
        s = fd_to_socket[fd]

    # 如果住服务器套接字可读,那么表示有来自客户端的一个连接,用READ_ONLY标志注册这个新连接,以便监视通过它的数据
    # handle inputs
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # a readable socket is ready to accept a connection
                connection, client_address = s.accept()
                print(' connection', client_address, file=sys.stderr)
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # give the connection a queue for data to send
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    # a readable client socket has data.
                    print(' received {!r} form {}'.format(data, s.getpeername()), file=sys.stderr)
                    message_queues[s].put(data)
                    # add output channel for response
                    poller.modify(s, READ_WRITE)
                else:
                    # interpret empty result as closed connection.
                    print(' closing', client_address, file=sys.stderr)

                    # stop listening for input on the connection.
                    poller.unregister(s)
                    s.close()

                    # remove message queue
                    del message_queues[s]
        elif flag & select.POLLHUP:
            # client hung up
            print(' closing', client_address, '(HUP)', file=sys.stderr)
            # stop listening for input on the connection
            poller.unregister(s)
            s.close()
        elif flag & select.POLLOUT:
            # socket is ready to send data. if there is any to send
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                # no message waiting, so stop checking.
                print(s.getpeername(), 'queue empty', file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print(' sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)
                s.send(next_msg)
        elif flag & select.POLLERR:
            print(' exception on', s.getpeername(), file=sys.stderr)
            # stop listening for input on the connection.
            poller.unregister(s)
            s.close()

            # remove message queue
            del message_queues[s]
