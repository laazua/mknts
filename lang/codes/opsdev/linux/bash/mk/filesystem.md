#### filesystem

- **文件系统API**
1.  /sys 用于向用户空间公开内核设备、驱动程序和其他内核信息.
2.  /proc 用于向用户空间公开内核设置、进程和其他内核信息.
3.  /dev 用于向用户空间公开内核设备节点.
4.  /run 作为用户空间套接字和文件的位置.
5.  /tmp 作为易失性临时用户空间文件系统对象(X)的位置.
6.  /sys/fs/cgroup(以及下面的文件系统)来公开内核控制组层次结构.
7.  /sys/kernel/security、/sys/kernel/debug (X)、/sys/kernel/config (X),用于向用户空间公开特殊用途的内核对象.
8.  /sys/fs/selinux 向用户空间公开 SELinux 安全数据.
9.  /dev/shm 作为用户空间共享内存对象的位置.
10. /dev/pts 用于向用户空间公开内核伪 TTY 设备节点.
11. /proc/sys/fs/binfmt_misc 用于在内核 (X) 中注册其他二进制格式.
12. /dev/mqueue，用于将 mqueue IPC 对象公开给用户空间 (X).
13. /dev/hugepages 作为用户空间 API 来分配"巨大"内存页面 (X).
14. /sys/fs/fuse/connections, 用于向用户空间公开内核 FUSE 连接 (X).
15. /sys/firmware/efi/efivars 用于向用户空间公开固件变量.