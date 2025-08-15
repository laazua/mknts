### firewalld

- **zone**

| zone   |     默认规则     |                         适用场景                             |
|:------:|:---------------:|:------------------------------------------------------------:|
| drop   | 丢弃所有传入流量 | 最高安全级别，适用于不信任的网络（如公共 Wi-Fi），丢弃所有未经请求的入站流量。|
| block  | 拒绝所有传入流量（返回 ICMP 拒绝消息）| 类似 drop，但会通知发送方连接被拒绝。适用于需要明确拒绝流量的场景。|
| public | 仅允许显式放行的传入流量 | 默认 zone，适用于公共网络（如咖啡馆、机场），仅开放必要的服务（如 HTTP/SSH）。|
| external | 仅允许指定传入流量，默认启用伪装（NAT）| 用于外部网络（如路由器防火墙），保护内部网络，通常允许 SSH 和伪装（IPv4 地址转换）。|
| internal | 允许大部分传入流量（信任内部用户）| 用于内部网络（如企业内网），允许 SSH、DHCP、Samba 等服务，信任内部设备。|
| dmz | 仅允许指定传入流量 | 用于隔离区（如暴露给外网的服务器），限制流量到特定服务（如 Web 服务器）。|
| work | 允许部分传入流量（信任工作环境）| 适用于工作场所，允许 SSH、DHCP、文件共享等，但限制高危服务。|
| home | 允许较多传入流量（信任家庭网络）| 家庭网络环境，允许打印机共享、DLNA、SSH 等，比 internal 更宽松。|
| trusted | 允许所有流量（完全信任）| 最高信任级别（如 VPN 或内部测试网络），无任何限制，慎用。|

- **说明**
1. 主机上的每个网络接口(ip a)只能绑定到一个zone上
2. 匹配顺序：先检查 来源 IP 绑定的 zone，再检查 接口 绑定的 zone, 最后回退到 默认 zone（通常是 public）
3. 所有 zone 默认允许出站流量，但入站流量根据 zone 规则控制

- **rich-rule**
1. 基本语法: rule [family="ipv4|ipv6"] [source address="ip/MASK" mac="MAC地址"|destination address="IP/MASK"] [service name="服务名"|port port="端口号"|protocol value="协议名"] [log prefix="前缀文本" level="info"] [audit] [action] [other_options]
2. 示例：
```bash
# 允许特定IP访问指定服务
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.1.100" service name="ssh" accept'  
# 拒绝某网段的 ICMP 并记录日志
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="192.168.2.0/24" protocol value="icmp" log prefix="ICMP BLOCK: " level="warning" reject'  
# 限速http请求
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="10/minute" accept'  
# 端口转发(公网 8080 → 内网 80)
firewall-cmd --zone=external --add-rich-rule='rule family="ipv4" forward-port port="8080" protocol="tcp" to-port="80" to-addr="192.168.1.2"'  
# 临时生效指定时长(30秒)
firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="10.0.0.5" service name="http" accept' --timeout=30  
# 端口转发
# echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
# sudo sysctl -p
# 网卡接口绑定
#   外部接口（eth0）绑定到 external zone（默认启用伪装 masquerade）。
firewall-cmd --zone=external --change-interface=eth0 --permanent
#   内部接口（如 eth1）绑定到 internal zone。
firewall-cmd --zone=internal --change-interface=eth1 --permanent
# 使用 forward-port 参数实现 DNAT：
sudo firewall-cmd --zone=external --add-rich-rule='rule family="ipv4" forward-port port="8080" protocol="tcp" to-port="80" to-addr="192.168.1.100"' --permanent
# 允许 192.168.1.0/24 通过防火墙访问外网，并启用 SNAT
firewall-cmd --zone=external --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" masquerade' --permanent

```
- **特别说明**
1. 调试建议：先用 --timeout 测试临时规则，避免配置错误导致访问中断  
   firewall-cmd --zone=external --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" masquerade' --timeout 30