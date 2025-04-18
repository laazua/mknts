#!/bin/bash

if [[ ${UID} -ne 0 ]];then
  echo "请以root身份运行此脚本"
  exit 0
fi

# 查看磁盘数量
fdisk -l|grep ^Disk|grep -v identifier

disk_num=$(fdisk -l|grep ^Disk|grep -v identifier|wc -l)
if [[ ${disk_num} -eq 4]];then
  echo "磁盘已经分区"
  exit 0
fi

read -e -p "是否开始分区:[yes|no]" enter
if [[ "${enter}" != "yes" ]];then
  echo "请确认分区准备,退出当前脚本."
  exit 0
fi

# 确认分区挂载目录是否存在
if [[ ! -d /data ]];then
    mkdir /data
fi

umount /dev/vdb
fdisk /dev/vdb <<EOF
n
p
1


w
EOF

partx -a /dev/vdb
# 格式化磁盘
mkfs.ext4 /dev/vdb1
# 挂在磁盘到/data目录
mount /dev/vdb1 /data

# 重启机器自动挂载磁盘
echo "/dev/vdb1 /data ext4 defaults,noatime 0 0" >>/etc/fstab
