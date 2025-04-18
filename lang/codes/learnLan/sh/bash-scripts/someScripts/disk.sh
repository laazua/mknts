#!/bin/bash

echo "
############ centos 重新调整分区大小 ###############
# 查看分区大小
[root@NextCloud ~]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root   50G   49G  1.6G   97% /
...
/dev/mapper/centos-home  965G   33M  965G    1% /home
...
​
# 卸载/home，卸载前记得备份cp -r /home/ homebak/ 我这里/home下没有什么文件，就不备份了
[root@NextCloud ~]# umount /home
[root@NextCloud ~]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root   50G   49G  1.6G   97% /
...

# 移除/home所在的lv
[root@NextCloud ~]# lvremove /dev/mapper/centos-home 
Do you really want to remove active logical volume centos/home? [y/n]: y
 Logical volume "home" successfully removed
​
# 增加/所在的lv，这里我们增加500G空间
[root@NextCloud ~]# lvextend -L +500G /dev/mapper/centos-root 
 Size of logical volume centos/root changed from 50.00 GiB (12800 extents) to 550.00 GiB (140800 extents).
 Logical volume centos/root successfully resized.
​
# 增加lv后查看/并没有增加，确认分区格式
[root@NextCloud ~]# df -hT
文件系统                类型      容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root xfs        50G   49G  1.6G   97% /
...
​
# 扩展/所在文件系统
[root@NextCloud ~]# xfs_growfs /dev/mapper/centos-root 
meta-data=/dev/mapper/centos-root isize=512    agcount=4, agsize=3276800 blks
 =                       sectsz=4096  attr=2, projid32bit=1
 =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=13107200, imaxpct=25
 =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=6400, version=2
 =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 13107200 to 144179200
​
# 查看分区大小
[root@NextCloud ~]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root  550G   49G  502G    9% /
...
​
# 确认Free PE可分配空间
[root@NextCloud ~]# vgdisplay
 --- Volume group ---
 VG Name               centos
 System ID 
 Format                lvm2
 Metadata Areas        1
 Metadata Sequence No  7
 VG Access             read/write
 VG Status             resizable
 MAX LV                0
 Cur LV                3
 Open LV               2
 Max PV                0
 Cur PV                1
 Act PV                1
 VG Size               <1023.00 GiB
 PE Size               4.00 MiB
 Total PE              261887
 Alloc PE / Size       168416 / <657.88 GiB
 Free  PE / Size       93471 / 365.12 GiB
 VG UUID               TDRsyJ-GZ2H-ZRWr-Gfje-LNe1-ggpz-0pJ7jx
​
# 创建home lv分区
[root@NextCloud ~]# lvcreate -L 100G -n home centos
 Logical volume "home" created.
​
# 格式化home分区
[root@NextCloud ~]# mkfs.xfs /dev/centos/home
meta-data=/dev/centos/home       isize=512    agcount=4, agsize=6553600 blks
 =                       sectsz=4096  attr=2, projid32bit=1
 =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=26214400, imaxpct=25
 =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=12800, version=2
 =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
​
# 挂载/home
[root@NextCloud ~]# mount /dev/centos/home /home
​
# 查看分区大小
[root@NextCloud ~]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
/dev/mapper/centos-root  550G   49G  502G    9% /
...
/dev/mapper/centos-home  100G   33M  100G    1% /home
...
"