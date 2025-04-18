#!/bin/bash
yum update nss
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh http://www.elrepo.org/elrepo-release-6-8.el6.elrepo.noarch.rpm
yum --enablerepo=elrepo-kernel -y install kernel-ml
yum --enablerepo=elrepo-kernel -y install kernel-lt

cp /etc/grub.conf /etc/grub.conf.bak
sed -i 's/default=1/default=0/g' /etc/grub.conf

echo "当前系统内核版本"
uname -r
echo "请重启系统！查看系统版本是否升级成功."
