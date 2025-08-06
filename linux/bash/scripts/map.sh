#!/bin/bash
#

ips=(
  "1 10.8.0.1"
  "2 10.8.0.2"  
)

for ip in "${ips[@]}";do
    set -- $ip
    echo key: $1 value: $2
done