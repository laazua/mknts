# OpenVPN 2.5.8 搭建

- 安装 openvpn 软件  
  ubuntu: apt install openvpn

- 下载 EasyRSA-3.0.8.tgz 并生成相关证书(下面的 server 参考包中包含了 EasyRSA-3.0.8.tgz)

- 分别对 openvpn 的服务端和客户端进行配置

- 启动 openvpn 的服务端和客户端

- [server 参考](./openvpn-server.tar.gz)
- [client 参考](./openvpn-client.tar.gz)

* _openvpn 服务端配置_

```
port 1194
proto tcp
dev tun
ca /etc/openvpn/server/pki/ca.crt
cert /etc/openvpn/server/pki/issued/server.crt
key /etc/openvpn/server/pki/private/server.key  # This file should be kept secret
dh /etc/openvpn/server/pki/dh2048.pem
# 这里是openvpn server的IP地址池
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist /var/log/openvpn/ipp.txt
push "route dhcp-option DNS 114.114.114.114"
push "route dhcp-option DNS 8.8.8.8"
client-to-client
duplicate-cn
keepalive 10 120
tls-auth /etc/openvpn/server/pki/ta.key 0 # This file is secret
cipher AES-256-CBC
user root
group root
persist-key
persist-tun
status /var/log/openvpn/openvpn-status.log
verb 3
# 下发给客户端的需要走VPN的网络流量，其它网段不走VPN，可正常上网
push "route 12.168.165.88 255.255.255.0"
```

- _openvpn 服务端所在服务器配置_

```
# ip转发
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p

# -s 跟目标网络地址 -o 服务器主机的网络网卡
iptables -t nat -A POSTROUTING -s 10.8.0.0/16 -o ens160 -j MASQUERADE # 网络设备为ens160
```

- _openvpn 客户端配置_

```
client
dev tun
proto tcp
# openvpn服务端地址
remote 192.168.165.83 1194
nobind
persist-key
persist-tun
remote-cert-tls server
ca /etc/openvpn/client/pki/ca.crt
cert /etc/openvpn/client/pki/issued/client.crt
key /etc/openvpn/client/pki/private/client.key
tls-auth /etc/openvpn/client/pki/ta.key 1
dh /etc/openvpn/client/pki/dh2048.pem
verb 3
```

- _openvpn 客户端所在服务器配置_

```
# 路由配置 ip route add 目标服务器地址 via vpn虚拟网关
ip route add 192.168.165.88 via 10.8.0.5
```
