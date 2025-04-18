# -*-coding:utf-8-*-

"""
unix domain sockets
"""

import socket
import os


server_address = './uds_socket'

# make sure the socket does not exis
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# create a uds socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# bind the socket to the address
print('starting up on {}'.format(server_address))
sock.bind(server_address)
# listen for incoming connections
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address =  sock.accept()
    try:
        print('connection from ', client_address)
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()

