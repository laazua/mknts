#!/bin/bash

## http://www.ansible.com.cn/

## 部署要求
# 防火墙规则制定
# ss免密登录
# 时间同步

# master生成公私钥
# ssh-keygen
# ssh-copy-id -i id_rsa.pub root@ip:~/.ssh    将公钥拷贝到节点机器上去

## 免交互创建公私钥
# ssh-keygen -f /root/.ssh/ -N ""
## 免交互传递公钥
# yum install sshpass
# sshpass -p123456 ssh-copy-id -o StrictHostKeyChecking=no -i /root/.ssh/id_rsa.pub user@ip

## ansible安装
# yum isntall ansibale

## Usage:
# ansible 被操作的机器或组名 -m 模块 -a "参数1=值1 参数2=值2 ..."

## 常用模块

# hostname模块
# ansible -m hostname -a "name=node1" 192.168.22.1

# file模块
# path        文件绝对路径
# state       操作(touch文件, absent删除, link软链接, hard硬链接, directory目录创建)
# owner       设置所有者
# group       设置所属组
# mode        设置权限0000
# recurse     递归yes or no
# ansible -m file group -a "path=/tmp/test state=touch"
# ansible -m file group -a "path=/tmp/test.txt state=absent"
# ansible -m file group -a "path=/tmp/test.txt owner=test group=test mode=0600"
# ansible -m file group -a "src=/tmp/test path=/tmp/test_rs state=link"
# ansible -m file group -a "src=/tmp/test path=/tmp/test_hk state=hard"
# ansible -m file group -a "path=/tmp/test state=directory"
# ansible -m file group -a "path=/tmp/test owner=test mode=0600 recurse=yes"

## copy模块
# src         文件源路径   注意路径最后是否有/：有'/'表示把目录下的所有文件拷贝到目标机器,没有'/'表示把整个目录拷贝到目标机器上
# dest        目标路径
# content     往目标文件输入内容
# force       强制yes or no
# backup      是否备份有冲突的源文件[文件名相同,内容不同] yes or no
# checksum    拷贝完整性校验,使用sha1sum生成校验码
# owner       目标文件所有者
# group       目标文件所属组
# mode        目标文件权限
## sha1sum  test.txt   =>  f8182e...
## ansible -m copy group -a "src=/root/test.txt dest=/tmp checksum=f8182e... owner=test group=test mode=0600"
# ansible -m copy group -a "content='aaaaaa' dest=/tmp/test.txt force=no"

## fetch把节点机器上的文件拷贝到master机器上
# ansible -m fetch group -a "src=/tmp/test.txt dest=/tmp/"

## user模块,管理用户账号和用户属性
# name                      指定用户名
# password                  指定密码
# state=absent|present      删除|创建
# system=yes|no             是否为系统用户
# shell=""                  指定登录shell
# generate_ssh_key=yes|no   是否创建密钥对
# uid=                      指定用户的uid
# append=yes|no             用户是否追加到其他组
# group=                    用户所属组
# groups=                   将现有用户加入到某个组,空值就会把该用户从所有组中删除
# create_home=yes|no        是否建立家目录
# remove=yes|no             删除家目录

## group模块,管理用户组和用户组属性
# name=                     组名
# state=persent|absent      创建|删除
# system=yes|no             是否为系统组
# gid                       gid

## cron模块,管理周期性时间任务
# name                      计划任务的名称
# user                      执行计划任务的用户
# job                       计划任务命令
# minute                    计划任务的分 默认*
# hour                      计划任务的时 默认*
# day                       计划任务的日 默认*
# month                     计划任务的月 默认*
# week                      计划任务的周 默认*
# state absent              删除计划任务
# ansible -m cron group -a "name='cron test' user=root job='echo haha >/tmp/test.txt' minute=23"
# ansible -m cron group -a "name='cron test' state=absent"

## yum_repository模块,用于配置yum仓库
# name                      仓库名 name.repo源的名称[name]
# description               描述
# baseurl                   包下载路径
# gpgcheck=1|0              包gpg验证
# enabled=yes|no            是否开源本源
# state=basent              删除源

## yum模块,软件包的安装与卸载
# name                                          需要安装软件包的名称
# list=installed|updates|available|repos        列出已经安装|需要更新|可获得的|yum源
# state=absent|removed|installed|present|latest 删除|删除|安装确认|安装确认|安装最新版本

## service模块
# name                                          服务名称
# state=reloaded|restarted|started|stopped      服务管理
# enabled yes|no                                开启是否启动
# ansible -m service group -a "name=vsftpd state=started enabled=on"

## script模块,远程机器上执行本地脚本
# ansible -m script group -a "/root/test.sh"

## command和shell模块
# 两个模块都是用于执行linux命令,command模块不能执行一些类似$HOME,>,<|等符号,但shell可以
# ansible -m command group -a "ls /root"
# ansible -m shell group -a "echo 'hello' > /tmp/test.txt"

## setup模块,收集远程机器的基本信息(系统类型,主机名,ip,cpu,mem等)
# ansible_all_ipv4_address            显示ipv4信息
# ansible_devices                     显示磁盘设备信息
# ansible_distribution_major_version  显示系统主版本
# ansible_distribution_version        显示系统版本
# ansible_machine                     显示系统类型
# ansible_lvm                         显示lvm相关信息
# ansible_memtotal_mb                 显示系统总内存
# ansible_memfree_mb                  显示系统可用内存
# ansible_memory_mb                   显示系统详细内存情况
# ansible_swaptotal_mb                显示系统总的swap
# ansible_swapfree_mb                 显示系统可用swap
# ansible_mounts                      显示系统磁盘挂在情况
# ansible_processor                   显示系统cpu个数
# ansible_processor_vcpus             显示cpu个数      
# ansible -m setup group -a "filter=ansible_processor"

## stat模块,获取文件的状态信息
# ansible -m stat group -a "path=/tmp/test.txt"

## ansible-galaxy
# https://galaxy.ansible.com/