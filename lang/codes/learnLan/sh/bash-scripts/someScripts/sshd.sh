#!/bin/bash
# sshd免密登陆


## master host operation
# ssh-keygen -t rsa
# scp id_rsa.pub gamecpp@172.16.9.124:~/.ssh
# echo "Host 172.16.9.124" >> /root/.ssh/config
# echo "  user gamecpp" >> /root/.ssh/config
# echo "  port 4521" >> /root/.ssh/config

## node host operation
# cat /home/gamecpp/.ssh/id_rsa.pub > /home/gamecpp/.ssh/authorized_keys
# chmod 700 /home/gamecpp/.ssh && chmod 600 /home/gamecpp/.ssh/authorized_keys
# sed -i 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
# sed -i 's/#Port 22/Port 4521/g' /etc/ssh/sshd_config
# systemctl restart sshd
