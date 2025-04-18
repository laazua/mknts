#!/bin/bash

## vmware nat模式下的网络配置

## vmware配置:
# 虚拟机 => 网络适配器 => NAT模式
# 编辑 => 虚拟网络编辑器 => NAT模式(VMnet8) => NAT设置 => 配置主机端口和虚拟机ip:port(主机端口用于ssh连接端口)
# 虚拟机的网络配置为静态获取ip地址,其中ip地址为上一步骤中设置的虚拟ip

## xshell连接:
# xshell: ssh 127.0.0.1 port
