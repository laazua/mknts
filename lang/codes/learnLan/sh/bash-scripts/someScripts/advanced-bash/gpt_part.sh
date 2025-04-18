#!/bin/bash
# gpt分区

# parted # 进入parted工具，输入help可查看帮助

# select /dev/sda # 选择你要操作的设备，一定要注意，不要把默认设备误操作了

# mklabel gpt # 设定使用的分区类型, 如果要用MBR分区，输入msdos即可

# mkpart # 添加一个分区:  (parted) mkpart

# 输入分区名称，回车

# 输入使用哪种文件系统，默认ext2，回车 （此处可以随意选，之后重新格式化写入文件系统）: 文件系统类型？ [ext2]? xfs

# 输入分区从第几Mb的位置开始，输入1，从第1Mb开始（最好不要从0开始）
# Start? 1
# End? 14TB

# 此时已经分区成功，输入print查看目前分区情况

# mkfs.xfs /dev/sda

# mount /dev/sda /data/

# 获取UUID方法: blkid /dev/sda

# 通过/etc/fstab文件来实现开机自动挂载(vim /etc/fstab):
# UUID=1caf6563-3a4b-47d6-a4eb-cbcb6f17d830 /data			  xfs     defaults        0 0