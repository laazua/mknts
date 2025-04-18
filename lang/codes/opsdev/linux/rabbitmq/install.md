### 集群部署

- **节点系统**
1. debian 12

- **节点准备**
1. 192.168.165.81  
   192.168.165.82  
   192.168.165.83
2. 192.168.165.81: hostnamectl hostname node-01  
   192.168.165.82: hostnamectl hostname node-02
   192.168.165.83: hostnamectl hostname node-03
3. 所有节点重启: sudo reboot
4. rabbitmq-server的版本所对应的erlang版本安装([参考官网](https://www.rabbitmq.com/docs/install-debian)):
```bash
#!/bin/sh

sudo apt-get install curl gnupg apt-transport-https -y

## Team RabbitMQ's main signing key
curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null
## Community mirror of Cloudsmith: modern Erlang repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null
## Community mirror of Cloudsmith: RabbitMQ repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.9F4587F226208342.gpg > /dev/null

## Add apt repositories maintained by Team RabbitMQ
sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
## Provides modern Erlang/OTP releases
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/debian bookworm main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/debian bookworm main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/debian bookworm main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-erlang/deb/debian bookworm main

## Provides RabbitMQ
##
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-server/deb/debian bookworm main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.rabbitmq.com/rabbitmq/rabbitmq-server/deb/debian bookworm main

# another mirror for redundancy
deb [arch=amd64 signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-server/deb/debian bookworm main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.rabbitmq.com/rabbitmq/rabbitmq-server/deb/debian bookworm main
EOF

## Update package indices
sudo apt-get update -y

## Install Erlang packages
##
## For versions not compatible with the latest available Erlang series, which is the case
## for 3.13.x, apt must be instructed to install specifically Erlang 26.
## Alternatively this can be done via version pinning, documented further in this guide.
supported_erlang_version="1:26.2.5.6-1"
sudo apt-get install -y erlang-base=$supported_erlang_version \
                        erlang-asn1=$supported_erlang_version \
                        erlang-crypto=$supported_erlang_version \
                        erlang-eldap=$supported_erlang_version \
                        erlang-ftp=$supported_erlang_version \
                        erlang-inets=$supported_erlang_version \
                        erlang-mnesia=$supported_erlang_version \
                        erlang-os-mon=$supported_erlang_version \
                        erlang-parsetools=$supported_erlang_version \
                        erlang-public-key=$supported_erlang_version \
                        erlang-runtime-tools=$supported_erlang_version \
                        erlang-snmp=$supported_erlang_version \
                        erlang-ssl=$supported_erlang_version \
                        erlang-syntax-tools=$supported_erlang_version \
                        erlang-tftp=$supported_erlang_version \
                        erlang-tools=$supported_erlang_version \
                        erlang-xmerl=$supported_erlang_version
```

- **预编译压缩包准备**
1. github的rabbitmq-server仓库下载: rabbitmq-server-generic-unix-3.13.7.tar.xz
2. 将rabbitmq-server-generic-unix-3.13.7.tar.xz分发到所有节点上 && tar -xf rabbitmq-server-generic-unix-3.13.7.tar.xz -C /data
3. sudo chown -R zhangsan:zhangsan /data/rabbitmq_server-3.13.7

- **systemd管理**
1. vim /usr/lib/systemd/system/rabbitmq.service
```text
[Unit]
Description=RabbitMQ Messaging Server
After=network.target

[Service]
Type=simple
User=zhangsan
Group=zhangsan
WorkingDirectory=/data/rabbitmq_server-3.13.7
Environment="HOME=/data/rabbitmq_server-3.13.7"
ExecStart=/data/rabbitmq_server-3.13.7/sbin/rabbitmq-server
ExecStop=/data/rabbitmq_server-3.13.7/sbin/rabbitmqctl stop
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```
2. systemctl daemon-reload && systemctl enable rabbitmq && systemctl start rabbitmq
3. 同步.erlang.cookie文件: cp -f ~/.erlang.cookie /data/rabbitmq_server-3.13.7/.erlang.cookie
3. 设置所有.erlang.cookie文件权限: chmod 400 .erlang.cookie
4. systemctl restart rabbitmq && /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl status

- **加入节点**
1. 同步所有节点上的.erlang.cookie文件与node-01一致: cp -f ~/.erlang.cookie /data/rabbitmq_server-3.13.7/.erlang.cookie
2. 设置所有.erlang.cookie文件权限: chmod 400 .erlang.cookie
3. cd /data/rabbitmq_server-3.13.7 && sbin/rabbitmqctl stop_app && sbin/rabbitmqctl join_cluster rabbit@node-01 && sbin/rabbitmqctl start_app

- **安装插件**
1. 所有节点执行: /data/rabbitmq_server-3.13.7/sbin/rabbitmq-plugins enable rabbitmq_management

- **添加管理员**
1. /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl add_user admin password
2. /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl set_user_tags admin administrator
3. /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

- **web管理页面**
1. 访问: http://192.168.165.81:15672


- **flags修复**
1. /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl -q --formatter pretty_table list_feature_flags   name state provided_by desc doc_url
2. /data/rabbitmq_server-3.13.7/sbin/rabbitmqctl enable_feature_flag detailed_queues_endpoint    # detailed_queues_endpoint显示disable
