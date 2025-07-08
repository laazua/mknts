### NetworkManager 

- 静态ip配置
```bash
# 查看网络接口设备
sudo nmcli d status
# 配置静态ip
sudo nmcli c mod ens192 ipv4.addresses 192.168.165.82/24 ipv4.gateway 192.168.165.254 ipv4.dns "8.8.8.8 114.114.114.114" ipv4.method manual
# 重启网卡
sudo nmcli c down ens192 && sudo nmcli c up ens192

## 以上操作对应配置: /etc/NetworkManager/system-connections/ens192.nmconnection
```
