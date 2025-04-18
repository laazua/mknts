### debian

- **sudo配置**
1. apt install sudo/stable
2. cat /etc/sudoers.d/zhangsan
```bash
zhangsan  ALL=(ALL) NOPASSWD: ALL
```

- **静态IP配置**
1. 方式1: vim /etc/network/interfaces
```bash
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
#allow-hotplug ens192
#iface ens192 inet dhcp
#
auto ens192
iface ens192 inet static
    address 192.168.165.87
    netmask 255.255.255.0
    gateway 192.168.165.254
    nameservers 8.8.8.8 114.114.114.114
```

2. 方式二: vim /etc/netplan/00-installer-config.yaml
```bash
network:
  ethernets:
    ens33:
      dhcp4: false
      dhcp6: false
      addresses:
        - 192.168.165.89/24
      routes:
        - to: default
          via: 192.168.165.254
      nameservers:
        addresses:
          - 8.8.8.8
          - 114.114.114.114
  version: 2
```
