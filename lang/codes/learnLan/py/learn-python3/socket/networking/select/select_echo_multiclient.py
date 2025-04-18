# -*-coding:utf-8-*-
import socket
import sys


messages = [
    'this is the message',
    'it will be sent',
    'in parts.',
]

server_address = ('127.0.0.1', 8888)

# create a TCP/IP socket.
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# connect the socket too the part where the server is listening.
print('connection to {} port {}'.format(*server_address), file=sys.stderr)
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()
    # send messages on both sockets.
    for s in socks:
        print('{}: sending {!r}.'.format(s.getpeername(), outgoing_data), file=sys.stderr)
        s.send(outgoing_data)

    # read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print('{}: received {!r}'.format(s.getpeername(), data), file=sys.stderr)
        if not data:
            print('closing socket', s.getpeername(), file=sys.stderr)
            s.close()
