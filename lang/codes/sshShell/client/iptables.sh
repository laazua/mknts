#!/bin/bash

## iptables ruls
## author: Sseve
## date: 2021-08-19

IPT_CMD="/usr/sbin/iptables"
IPT_SAV="/usr/sbin/iptables-save"

if [[ ! -x ${IPT_CMD} ]] && [[ ! -x ${IPT_SAV} ]]; then
  echo -e "\033[31miptables tool not exist.\033[0m"
  exit 1
fi

# INPUT chain
${IPT_CMD} -P INPUT ACCEPT
${IPT_CMD} -F
${IPT_CMD} -A INPUT -i lo -p all -j ACCEPT
${IPT_CMD} -A OUTPUT -o lo -p all -j ACCEPT

${IPT_CMD} -A INPUT -p tcp -m multiport --dports 22,80,3306,4521,33060 -j ACCEPT

#${IPT_CMD} -A INPUT -s 0.0.0.0/0 -p tcp --dport 5000:5010 -j ACCEPT

${IPT_CMD} -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

${IPT_CMD} -P INPUT DROP

${IPT_SAV} > /etc/sysconfig/iptables-config