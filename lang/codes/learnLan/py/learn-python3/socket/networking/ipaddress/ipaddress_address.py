# -*-coding:utf-8-*-


"""
ipaddress模块包括处理IPv4和IPv6网络地址的类.这些类支持验证,查找网络上的主机和地址,以及其他操作
"""

import binascii
import ipaddress


AAADDRESSES = [
    '10.9.0.6',
    'ffd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

# 将一个字符串,整数,或字节序列传递给ip_address()以构造一个地址,返回值将是IPv4 address或IPv6 address实例.
for ip in AAADDRESSES:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('    IP version: ', addr.version)
    print('    is private: ', addr.is_private)
    print('    packed form:', binascii.hexlify(addr.packed))
    print('    integer: ', int(addr))


# 网络是由一系列地址定义的,它通常用一个地址和一个掩码来表示,该掩码表示地址的哪些部分表示网络,以及剩余的哪些部分表示网络上的地址.掩码可以
# 显示的表示，也可以像下面的例子那样使用前缀长度值.
NETWORKS = [
    '10.9.0.0/24',
    'ffd:875b:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print('    is private: ', net.is_private)
    print('    broadcast: ', net.broadcast_address)
    print('    compressed: ', net.compressed)
    print('    with netmask: ', net.with_netmask)
    print('    with hostmask: ', net.with_hostmask)
    print('    num addresses: ', net.num_addresses)

# 网络实例是可迭代的,并产生网络上的地址,但并非所有地址都有效,如首地址和广播地址使用host()方法
for ne in NETWORKS:
    net = ipaddress.ip_network(ne)
    print('{!r}'.format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)

# 除了迭代,网络实例还支持in操作来确定一个网络地址是否是网络中的一部分
ADDRESSES = [
    ipaddress.ip_address('10.9.0.6'),
    ipaddress.ip_address('10.7.0.31'),
    ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'),
    ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
]

for ip in ADDRESSES:
    for net in NETWORKS:
        if str(ip) in net:
            print('{}\nis on {}'.format(ip, net))
            break
        else:
            print(' {}\n is not on a known network'.format(ip))

# 网络接口表示网络上特定地址,可以用主机地址和网络前缀或网络掩码表示
for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print('{!r}'.format(iface))
    print('network:\n ', iface.network)
    print('ip:\n ', iface.ip)
    print('IP with prefixlen:\n ', iface.with_prefixlen)
    print('netmask:\n ', iface.with_netmask)
    print('hostmask\n ', iface.with_hostmask)
