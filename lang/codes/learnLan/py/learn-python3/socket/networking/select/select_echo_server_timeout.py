# -*-coding:utf-8-*-
import select
import socket
import queue
import sys


# create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# bind the socket to the port
server_address = ('127.0.0.1', 8888)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# listen for incoming connections
server.listen(5)

# select()的参数是3个列表,包含要监视的通信信道,第一个列表包含要读取的数据,第二个列表包含对象将接收发出的数据,第三个列表包含可能有错误的
# 对象.
# sockets from which we expect to read
inputs = [server]

# sockets to which we expect to write
outputs = []

# outgoing message queues (socket: Queue)
message_queues = {}

# 超时设置
TIMEOUT = 60

# 服务器主要部分调用select()来阻塞并等待网络活动
while inputs:
    # wait for at least one of the sockets to be ready for processing
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs, TIMEOUT)    # 超时60妙

    # handle inputs
    for s in readable:
        if s is server:
            # A 'readable' socket is ready to accept a connection.
            connection, client_address = s.accept()
            print(' connection from ', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # give the connection a queue for data. we want to send
            message_queues[connection] = queue.Queue()
        else:
            # 与一个已经发送数据的客户端建立连接
            data = s.recv(1024)
            if data:
                # a readable client socket has data
                print(' received {!r} from {}'.format(data, s.getpeername()), file=sys.stderr)
                message_queues[s].put(data)

                # ad output channel for response.
                if s  not in outputs:
                    outputs.append(s)
            else:
                # interpret empty result as closed connection
                print(' closing', client_address, file=sys.stderr)
                # stop listening for input on the connection.
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # remove message_queue.
                del message_queues[s]

    # handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # no messages waiting, so stop checking for writablity
            print(' ', s.getpeername(), 'queue empty', file=sys.stderr)
            outputs.remove(s)
        else:
            print(' sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)
            s.send(next_msg)

    # handle 'exceptional conditions.'
    for s in exceptional:
        print('exception condition on', s.getpeername(), file=sys.stderr)
        # stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # remove message queue
        del message_queues[s]
