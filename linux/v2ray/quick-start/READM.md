### v2ray

- 快速开始
1. 三种协议配置快速启动v2ray服务

- 启动服务
```bash
#### 选用以下一种方式启动服务端
# 1. vmess协议
mv vmess-server.json config.json && v2ray run -c config.json
# 2. vless协议
mv vless-server.json config.josn && v2ray run -c config.json
# 3. shadowsocks协议
mv shadowsocks-server.json config.json && v2ray run -c config.json
#### 启动客户端
# 1. vmess协议
mv vmess-client.json config.json && v2ray run -c config.json
# 2. vless协议
mv vless-client.json config.json && v2ray run -c config.json
# 3. shadowsocks协议
mv shadowsocks-client.json config.json && v2ray run -c config.json
```