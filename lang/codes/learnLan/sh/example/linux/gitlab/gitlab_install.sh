#!/bin/bash

# gitlab是私有的代码管理仓库系统

# 安装依赖
yum install -y policycoreutils openssh-server openssh-clients postfix

# 设置ssh服务&设置开机启动
systemctl enable sshd && systemctl start sshd

# 设置postfix服务&设置开机启动
systemctl enable postfix && systemctl start postfix

# 开放ssh以及http服务,然后重新加载防火墙列表
firewall-cmd --add-service=ssh --permanent
firewall-cmd --add-service=http --permanent
firewall-cmd --reload

#下载gitlab包并安装
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el6/gitlab-ce-12.4.2-ce.0.el6.x86_64.rpm
rpm -ivh gitlab-ce-12.4.2-ce.0.el6.x86_64.rpm

# 修改gitlab配置
# vi /etc/gitlab/gitlab.rb
# 修改gitlab访问地址的端口,默认为80,改为82

# 重新加载gitlab配置并启动
gitlab-ctl reconfigure
gitlab-ctl restart

# 防火墙端口放行
firewall-cmd --zone=public --add-port=82/tcp --permanent
firewall-cmd --reload


# gitlab创建组&&仓库&&用户&&分配权限
