#### disk

- **分区**
1. 安装工具: apt install fdisk/stable
2. 查看磁盘: fdisk -l
3. 创建分区: fdisk /dev/sdb
```text
Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (1-4, default 1): 
First sector (2048-83886079, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-83886079, default 83886079): +39G

Created a new partition 1 of type 'Linux' and of size 39 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```
4. fdisk -l && mkfs.ext4 /dev/sdb1
5. mkdir /data && mount /dev/sdb1 /data && df -h