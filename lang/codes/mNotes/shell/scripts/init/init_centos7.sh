#!/bin/bash 

######## centos7 init script ##########



## 验证是否有账号存在空口令的情况
## awk -F: '($2 == ""){printf $1}' /etc/shadow

## 检查除了root以外是否还有其它账号的UID为0
## awk -F: '($3 == 0) {printf $1}' /etc/passwd

## crontab文件权限访问控制
chown root:root /etc/crontab 
chmod 400 /etc/crontab 
chown -R root:root /var/spool/cron 
chmod -R go-rwx /var/spool/cron 
chown -R root:root /etc/cron.* 
chmod -R go-rwx /etc/cron.*

## 建立恰当的警告banner: 
echo "Authorized uses only. All activity may be \ 
     monitored and reported." >>/etc/motd 
chown root:root /etc/motd 
chmod 644 /etc/motd 
echo "Authorized uses only. All activity may be \ 
     monitored and reported." >> /etc/issue 
echo "Authorized uses only. All activity may be \ 
     monitored and reported." >> /etc/issue.net

## 限制root登录到系统控制台: 
cat </etc/securetty tty1 tty2 tty3 tty4 tty5 tty6 END_FILE 
chown root:root /etc/securetty 
chmod 400 /etc/securetty

## 设置守护进程掩码 vi /etc/rc.d/init.d/functions 设置为 umask 022

## 禁止core dump: 
## cat <>/etc/security/limits.conf * soft core 0 * hard core 0 END_ENTRIES

##log_martians将进行ip假冒的ip包记录到/var/log/messages 其它核心参数使用CentOS默认值
chown root:root /etc/sysctl.conf 
chmod 600 /etc/sysctl.conf
