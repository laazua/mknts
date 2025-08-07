### unbound

- 说明配置openvpn dns解析

- 系统rocky-10.0

- 安装
1. dnf -y install unbound.x86_64

- 配置:
1. cat /etc/unbound/conf.d/ovpn.conf
```txt
server:
    interface: 10.8.0.1
    access-control: 10.8.0.0/24 allow
    local-zone: "ovpn." static
    local-data: "client01.ovpn. IN A 10.8.0.2"
    local-data: "client02.ovpn. IN A 10.8.0.3"
```

- 启动unbound服务
1. systemctl start unbound


- 配置主机dns解析
```shell
ip a   # 查看主机网卡: ens160
nmcli c show   # 查看网卡连接情况
nmcli c mod ens160 ipv4.dns "10.8.0.1 8.8.8.8"
nmcli c down ens160 && nmcli c up ens160  # 查看配置dns解析：cat /etc/resolv.conf
```