#!/bin/bash
# 此脚本用于将主机上采集到的进程信息发送到promethues的http地址

z=$(ps aux|grep javapro)
while read -r z;do
    # 拼接变量
    var=$var$(awk '{print "cpu_usage{process=\""$1"\", pid=\""$2"\"}", $3z}');
    echo $var
done <<< "$z"

#curl -X POST -H  "Content-Type: text/plain" --data "$var" http://localhost:9091/metrics
echo "$var" |  curl --data-binary @- http://39.108.102.49:9091/metrics/job/top/instance/"127.0.0.1"
