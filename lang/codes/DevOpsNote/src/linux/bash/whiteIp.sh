#!/usr/bin/bash

set -e

iptables -F
iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT


iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A INPUT -p tcp --dport 1122 -j ACCEPT
iptables -A INPUT -p tcp --dport 6666 -j ACCEPT
iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
iptables -A INPUT -p tcp --dport 8877 -j ACCEPT
