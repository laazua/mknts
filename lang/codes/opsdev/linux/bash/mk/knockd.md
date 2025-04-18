### knockd

- 端口敲门
1. 安装: sudo apt install  knockd/stable
2. 配置: /etc/knockd.conf
```bash
[options]
	UseSyslog
        interface = ens33

[openSSH]
	sequence    = 7000,8000,9000
	seq_timeout = 5
	command     = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9000,8000,7000
	seq_timeout = 5
	command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[openHTTPS]
	sequence    = 12345,54321,24680,13579
	seq_timeout = 5
	command     = /usr/local/sbin/knock_add -i -c INPUT -p tcp -d 443 -f %IP%
	tcpflags    = syn
```
3. 登录端打开ssh端口: knock -v ip 7000 8000 9000
4. 登录端关闭ssh端口: knock -v ip 9000 8000 7000