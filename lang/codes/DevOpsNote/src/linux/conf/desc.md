# linux系统一些配置

* **历史命令时间戳** 
```
export HISTTIMEFORMAT="%F %T "添加至/etc/profile文件的最后  
source /etc/profile  
```

* **系统用户操作记录**
```
cat /etc/profile.d/auditlog.sh

log_command() {
    # 获取最后一条历史记录
    local uid=$(id -u)
    local command=$(history 1)
    # 记录日志到执行位置(可以将此文件存放到比较隐秘的位置)
    local logfile="/var/log/user_options-$(date "+%Y-%m-%d").log"
    if [ ! -f "$logfile" ];then
        touch "$logfile" && chmod 666 "$logfile"
    fi
    if [ $uid -ne 0 ];then
	    echo "## TIME: $(date "+%Y-%m-%d %H:%M:%S") ## USER IP: $(who | awk '{print $1,$5}'|awk 'NR==1') ## CMD: $command" >>"$logfile"
    else
        echo "## TIME: $(date "+%Y-%m-%d %H:%M:%S") ## USER IP: $(who | awk '{print $1,$5}'|awk 'NR==1') ## [su] ## CMD: $command" >>"$logfile"
    fi
}

# 配置到用户的登陆配置文件中
# PROMPT_COMMAND="log_command"

# 说明定义在/etc/profile.d/目录下的.sh文件里的函数都可以被系统用户调用
```

* **systemd service**
```
[Unit]
Description=Doris FE
After=network-online.target
Wants=network-online.target

[Service]
Type=forking
User=root
Group=root
LimitCORE=infinity
MemoryLimit=2048M
LimitNOFILE=200000
Restart=on-failure
RestartSec=30
StartLimitInterval=120
StartLimitBurst=3
KillMode=none
ExecStart=/usr/local/doris-2.0.5/fe/bin/start_fe.sh --daemon 
ExecStop=/usr/local/doris-2.0.5/fe/bin/stop_fe.sh

[Install]
WantedBy=multi-user.target
```


* **防火墙审计**
```
- firewall-cmd --set-log-denied=unicast
- firewall-cmd --reload
- cat >/etc/rsyslog.d/firewalld.conf<<EOF
:msg,contains,"_DROP" /var/log/firewalld.log
& stop
:msg,contains,"_REJECT" /var/log/firewalld.log
& stop
EOF

- systemctl restart rsyslog

- cat firewall-audit.sh <<EOF

#!/usr/bin/bash

cat /var/log/firewalld.log|awk '{print $10"="$17":"$19}'|grep -vE "SRC=0000*|SRC=fe80*"|grep DPT >/tmp/deny_analyze
cat /var/log/firewalld.log|awk '{print $10"="$18":"$20}'|grep -vE "SRC=0000*|SRC=fe80*"|grep DPT >>/tmp/deny_analyze
cat /tmp/deny_analyze|awk -F'=' '{gsub("PROTO", "协议", $3);gsub("DPT", "", $4);print $2"->"$3"/"$4$5}'|sort -nr|uniq -c|sort -nr| head -n 10

EOF
```

* **sshd配置唯一用户指定时间段登陆主机**
```
zhangsang@k8s-master-01:~$ cat /etc/ssh/sshd_config.d/a.conf 
AllowUsers huheng

Match user huheng
    ForceCommand  /usr/local/bin/loginlimit.sh

# 允许指定用户@主机
# AllowUsers zhangsan@192.168.165.88

zhangsan@k8s-master-01:~$ cat /usr/local/bin/loginlimit.sh 
#!/bin/bash

# 获取当前小时
current_hour=$(date +"%H")

# 指定时间段
if [ $current_hour -ge 8 ] && [ $current_hour -lt 23 ]; then
    # 在这个时间段内执行绵密登陆的操作，比如直接退出
    exec "$SHELL"
else
    # 不在这个时间段内执行的操作，比如提醒用户无法登陆
    echo "现在不是允许的登陆时间段，请在指定时间段内登陆。"
    exit 1
fi
```

* **systemctl edit 默认编辑器配置**
```
echo "export EDITOR=vim" >> ~/.bashrc
```

* **vim多行缩进**
vim ~/.vimrc
```
set shiftwidth=4
set expandtab
set tabstop=4

##  多行缩进!!!
# 进入可视行模式:
#   按shift + v 进入可视行模式
# 选择多行:
#   使用 j 或 k 键选择你想缩进的多行
# 缩进:
#   按shift + > 键进行缩进
# 取消缩进:
#   按shift + < 键取消缩进

## 多行注释!!!
# 进入可视行模式:
#   按shift + v 进入可视行模式
# 选择多行:
#   使用 j 或 k 键选择你要注释的多行
# 进入命令模式:
#   按shift + : 进入命令模式,此时你会看到 :'<,'>
# 添加注释符号:
#   在命令模式下输入 s/^/# / 并按 Enter 键. 这会在所选的每一行前添加#

## 宏录制和执行
# 录制:
#   qz定义一个名为z的宏 => recording @z
#   进入编辑模式: a或i => -- INSERT --recording @z
#   输入编辑的内容
#   esc && q 保存宏
# 执行:
#   将光标移动到想要执行宏的位置键入@z运行宏
```

* **日志审计**  
sudo vim /etc/profile.d/audit.sh  
```
export PROMPT_COMMAND='RETER_VAL=$?;logger -p local6.debug "$(whoami)[$$]: $(history 1| sed "s/^[ ]*[0-9]\+[ ]*//") [$RETER_VAL]"'
readonly PROMPT_COMMAND
```
sudo vim /etc/rsyslog.d/history.conf  
```
# 配置日志记录到执行地方
local6.debug /var/log/users-command.log
```
sudo systemctl restart rsyslog.service
