#!/bin/bash

## 加载配置
source ../conf/main.cfg
echo "${TEST}"


## 加载模块
source ../func/host_mon.sh
cpu_mon
mem_mon