#!/bin/bash

## 参加quick reference ##

# 远程主机执行本地脚本
# ssh username@ip bash < local_shell.sh

# 从服务器上压缩并下载
# ssh username@ip "tar czvf - ~/source" > output.tgz

# ssh代理跳转
# ssh -J proxy_host dest_host
# ssh多次代理跳转
# ssh -J username@proxy_host_1:username@proxy_host_2 dest_host