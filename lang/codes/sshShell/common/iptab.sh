#!/bin/bash

##并发控制实例
# iptables -I INPUT -p tcp --dport 80 -s 源IP -m connlimit --connlimit-above 10 -j REJECT

##组成: 四表 + 五链(hook_point) + 规则
# 四表: filter, nat, mangle, raw
# 五链: INPUT, OUTPUT, FORWARD, PREROUTING POSTROUTING

##数据包在表和链中的数据流向
#                         (filter,mangle)   
#    (nat,mangle,raw)| =>     FORWARD     => |
#  in => PREROUTING  |                       |  => POSTROUTING => out
#                    | => INPUT => OUTPUT => |     (nat,raw,mangle)
#                  (filter,mangle) (filter,nat,mangle,raw)

##规则组成
# 数据包访问控制: ACCEPT, DROP, REJECT
# 数据包改写: SNAT, DNAT
# 信息记录: LOG
#            table           command           chain            parameter&xmatch            target
#            -t filter       -A                INPUT            -p tcp                      -j ACCEPT
#               nat          -D                FORWARD          -s                             DROP
#               ...          -L                OUTPUT           -d                             REJECT
# iptables                   -F                PREROUTING       --sport                        DNAT
#                            -P                POSTROUTING      --dport                        SNAT
#                            -I                                 --dports
#                            -R                                 -m tcp
#                            -n                                    state
#                                                                  multiport

##白名单(policy ACCEPT)
# iptables -I INPUT -i lo -j ACCEPT
# iptables -A INPUT -p tcp --dport 22 -j ACCEPT
# iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 80:81 -j ACCEPT
# iptables -A INPUT -p icmp -j ACCEPT
# iptables -A INPUT  -m state --state ESTABLISHED,RELATED -j ACCEPT
# iptables -A INPUT -j REJECT 

##nat地址改写转发
# iptables -t nat -A POSTROUTING -s ip -j SNAT --to ip
# iptables -t nat -A PREROUTING -d ip -p tcp --dport 80 -j DNAT --to ip:port

##iptables防cc攻击
# iptables -I INPUT -p tcp --syn --dport 80 -m connlimit --connlimit-above 100 -j REJECT 
# iptables -A INPUT -P tcp -m limit --limit 3/m --limit-burst 10 -j ACCETP