# -*-coding:utf-8-*-
"""
address families: AF_INET, AF_UNIX
socket type: SOCK_DGRAM, SOCK_STREAM
"""

import socket
from urllib.parse import urlparse


# 查询主机系统名解析api,并将服务器的名称转换成其数字地址
print(socket.gethostbyname('www.baidu.com'))


# 服务器的更多命名信息
try:
    name, aliases, addresses = socket.gethostbyname_ex('www.baidu.com')
    print('Hostname: ', name)
    print('Aliases: ', aliases)
    print('Addresses: ', addresses)
except socket.error as msg:
    print('ERROR:', msg)


# 使用getfqdn()将部分名称转换成完全限定的域名
for host in ['apu', 'pymotw.com']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))

# 当服务器地址可用时,使用gethostbyaddr()对名称进行反向查找
try:
    hostname, aliases, addresses = socket.gethostbyaddr('14.215.177.38')
    print('Hostname: ', hostname)
    print('Aliases: ', aliases)
    print('Addresses: ', addresses)
except socket.error as msg:
    print('Error: ', msg)

# 查询服务信息
try:
    parsed_url = urlparse('https://www.python.com')
    port = socket.getservbyname(parsed_url.scheme)
    print('{:>6} : {}'.format(parsed_url.scheme, port))
except socket.error as msg:
    print('Error: ', msg)

# 反转查询服务端口
for port in [80, 443, 21, 25]:
    url = '{}://python.com/'.format(socket.getservbyport(port))
    print(url)

# 传输协议数字可以通过getprotobyname()获取
def get_constants(prefix):
    """
    创建一个字典,将套接字模块常量映射到他们的名称
    """
    return {
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }

protocols = get_constants('IPPROTO_')
for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(name, proto_num, const_name, getattr(socket, const_name)))

# 查询服务地址
families = get_constants('AF_')
types = get_constants('SOCK_')
for response in socket.getaddrinfo('www.python.org', 'http'):
    family, socktype, proto, cononname, sockaddr = response
    print('Family   :', families[family])
    print('Type     :', types[socktype])
    print('Protocol :', protocols[proto])
    print('Canonical name   :', cononname)
    print('Socket address   :', sockaddr)
