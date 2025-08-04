#!/bin/bash

### 放行端口

set -e

iptables -F
iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT


iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 6687 -j ACCEPT
iptables -A INPUT -p tcp --dport 6688 -j ACCEPT
