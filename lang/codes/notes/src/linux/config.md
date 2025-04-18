# 一些常用配置

---

- **sudo 配置特定账号免密使用特定命令**  
  cat /etc/sudoers.d/zhangsan

```
  zhangsan ALL=(ALL) NOPASSWD: /usr/bin/supervisorctl,/usr/bin/git
```

- **ubuntu 静态 ip 配置**  
  cat /etc/netplan/00-installer-config.yaml

```
  # This is the network config written by 'subiquity'

  network:
  ethernets:
  ens160:
  dhcp4: false
  dhcp6: false
  addresses: - 192.168.165.88/24
  routes: - to: default
  via: 192.168.165.254
  nameservers:
  addresses: - 8.8.8.8 - 114.114.114.114
  version: 2
```
