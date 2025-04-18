### 内核参数

- /etc/sysctl.conf

```
# 系统同时允许的最大连接数
# 此参数过大可能会导致系统性能下降或者消耗过多的内存资源(一般设置为几千,根据实际情况而定)
net.core.somaxconn = 1024
# 表示TCP SYN洪泛攻击的最大连接请求队列长度
net.ipv4.tcp_max_syn_backlog = 512
# 一般来说,net.ipv4.tcp_max_syn_backlog应该比net.core.somaxconn小,以避免 TCP SYN 洪泛攻击导致系统崩溃
```
