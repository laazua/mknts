#!/usr/bin/bash

set -e

zone="whiteips"

# 重置 firewalld
firewall-cmd --reload

# 清除默认规则（确保规则是干净的）
firewall-cmd --permanent --new-zone=$zone || true
firewall-cmd --permanent --delete-zone=$zone
firewall-cmd --permanent --new-zone=$zone

# 设置默认行为
firewall-cmd --permanent --zone=$zone --set-target=DROP

# 允许回环接口流量
firewall-cmd --permanent --zone=$zone --add-interface=lo
firewall-cmd --permanent --zone=$zone --add-source=127.0.0.1

# 允许已建立和相关的连接
# firewalld 默认允许 ESTABLISHED 和 RELATED 的连接，无需额外配置。

# 添加允许的端口
firewall-cmd --permanent --zone=$zone --add-port=1122/tcp
firewall-cmd --permanent --zone=$zone --add-port=6666/tcp
firewall-cmd --permanent --zone=$zone --add-port=8000/tcp
firewall-cmd --permanent --zone=$zone --add-port=8877/tcp

# 设置 $zone 为默认区域
firewall-cmd --set-default-zone=$zone

# 应用规则
firewall-cmd --reload
