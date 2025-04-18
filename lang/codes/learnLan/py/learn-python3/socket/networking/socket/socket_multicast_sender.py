# -*-coding:utf-8-*-
import socket
import struct
import sys


message = b'very important data'
multicast_group = ('127.0.0.1', 8888)

# create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set a timeout so the socket does not block indefinitely when trying to receive data
sock.settimeout(5)

# set the time-to-live for messages to 1 so they do not go past the local network segment
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(data, server))
finally:
    print('closing socket')
    sock.close()
