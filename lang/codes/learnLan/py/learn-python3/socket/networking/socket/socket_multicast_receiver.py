# -*-coding:utf-8-*-
import socket
import struct


multicast_group = '127.0.0.1'
server_address = ('', 8888)

# create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# bind to the server address
sock.bind(server_address)

# tell the operating system to add the socket to the multicast group in all interfaces
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'. format(len(data), address))
    print(data)

    print('sending acknowledgement to ', address)
    sock.sendto(b'ack', address)
