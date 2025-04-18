#!/bin/bash

## init system
## author: Sseve
## date: 2021-08-19

##  sshpass 安装


GAME_USER="gamecpp"
GAME_PASS="djf3aDFD233HD1J"
WEB_URL="http://159.75.220.163:8000/"
SRC_DIR="/usr/local/src/"
PKGS=(epel-release-7-5.noarch.rpm libjemalloc.tar.gz usercmd id_rsa.pub mysql-8.0.26-el7-x86_64.tar my.cnf)

#http://opensource.wandisco.com/centos/7/svn-1.10/RPMS
yum -y update
yum -y localinstall epel-release-7-5.noarch.rpm 
yum -y install yum-fastestmirror 
yum -y install  wget vim lrzsz.x86_64 ntpdate net-tools.x86_64 bc.x86_64
yum -y install cyrus-sasl cyrus-sasl-plain cyrus-sasl-ldap
## mysql install 
yum -y localinstall https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
#yum -y install mysql-community-server
yum -y install mysql-community-client-5.7.35-1.el7.x86_64

# 下载包
[ -d ${SRC_DIR} ] && cd ${SRC_DIR}
for p in ${PKGS[@]};do
    wget ${WEB_URL}${p}
done



cat >/etc/yum.repos.d/wandisco-svn.repo <<-'EOF'
[WandiscoSVN]
name=Wandisco SVN Repo
baseurl=http://opensource.wandisco.com/centos/7/svn-1.10/RPMS/$basearch/
enabled=1
gpgcheck=0
EOF
yum install -y subversion


# update system character
sed -i 's/LANG="en_US.UTF-8"/LANG="zh_CN.UTF-8"/' /etc/locale.conf
source /etc/locale.conf

# add game user
useradd ${GAME_USER} && echo ${GAME_PASS}|passwd --stdin ${GAME_USER}
sed -i '/NOPASSWD/a gamecpp  ALL=(ALL)       NOPASSWD: ALL' /etc/sudoers
sed -i '/anywhere/a gamecpp  ALL=(ALL)       ALL' /etc/sudoers

# 免登录
mkdir /home/gamecpp/.ssh
mv ${SRC_DIR}id_rsa.pub /home/gamecpp/.ssh/authorized_keys && chown -R gamecpp.gamecpp /home/gamecpp/.ssh && chmod 700 /home/gamecpp/.ssh && chmod 600 /home/gamecpp/.ssh/authorized_keys

# update system time
timedatectl status|grep 'Time zone'
timedatectl set-local-rtc 1
timedatectl set-timezone Asia/Shanghai

# 创建定时任务
echo "* * * * * ntpdate -u pool.ntp.org >/dev/null 2>&1" >> /var/spool/cron/root
echo "* * * * * sh /root/scripts/collector.sh >/dev/null 2>&1" >> /var/spool/cron/root
echo "* * * * * sh /root/scripts/secondCrontab.sh >/dev/null 2>&1" >> /var/spool/cron/root

# kernel parameter
modprobe bridge
modprobe ip_conntrack
echo "modprobe ip_conntrack" >> /etc/rc.local
echo "modprobe bridge" >> /etc/rc.local
echo "ulimit -SHn 65535" >> /etc/profile
echo "* hard nofile 65535" >> /etc/security/limits.conf
echo "* soft nofile 65535" >> /etc/security/limits.conf
echo "* soft nproc 65535" >> /etc/security/limits.conf
echo "* hard nproc 65535" >> /etc/security/limits.conf
echo "* soft core unlimited" >> /etc/security/limits.conf
echo "* hard core unlimited" >> /etc/security/limits.conf

cat >>/etc/sysctl.conf<< EOF
net.ipv6.conf.all.disable_ipv6=1
fs.file-max=65535
net.ipv4.tcp_max_tw_buckets = 5000
net.ipv4.tcp_sack = 1
net.ipv4.tcp_rmem = 4096 87380 4194304
net.ipv4.tcp_wmem = 4096 16384 4194304
net.ipv4.tcp_max_syn_backlog = 65536
net.core.netdev_max_backlog = 32768
net.core.somaxconn = 65535

net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216

net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_syncookies = 1

net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1

net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_max_orphans = 3276800

net.ipv4.ip_local_port_range = 20000 65535
net.nf_conntrack_max  = 1048576

EOF
sysctl -p

# sshd
sed -i 's/#UseDNS yes/UseDNS no/g' /etc/ssh/sshd_config
mkdir -p /data/game
chown -R gamecpp.gamecpp /data/game
mkdir -p /home/gamecpp/.bana/ && chown -R gamecpp.gamecpp /home/gamecpp/.bana/ && chmod 700 /home/gamecpp/.bana/
curl ip.sb >/data/game/myip.txt

# game process lib
tar -xf libjemalloc.tar.gz -C /usr/local/lib
echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig

# host's option log record(usercmd => /usr/bin/usercmd)
mv usercmd /usr/bin/ && chmod +x /usr/bin/usercmd && [ -d /usr/bin/.hist/.cmd/ ] || mkdir -m 777 -p /usr/bin/.hist/.cmd
echo 'export SSH_CLIENT=$(/usr/bin/who am i | /bin/egrep -o "[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*")' >> /etc/profile.d/usercmd.sh
echo 'export SSH_TTY=$(who am i | tr -s " " | cut -d " " -f2)' >> /etc/profile.d/usercmd.sh
echo 'export PROMPT_COMMAND={ $(history 1 | { read x cmd;date=$(date "+%Y-%m-%d %T");/usr/bin/usercmd "$date ### IP:$SSH_CLIENT ### PS:$SSH_TTY ### USER:$USER ### $cmd"; });} >& /dev/null' >> /etc/profile

sed -i "s#\(.*PROMPT_COMMAND=\)\(.*\)\(null\)#\1'\2\3'#" /etc/profile.d/usercmd.sh
source /etc/profile.d/usercmd.sh
