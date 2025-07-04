# ssh相关配置

- 启用 SSH 多路复用
```
## 客户端配置
# mkdir ~/.ssh/cm_socket
# cat ~/.ssh/config 
Host *
    ControlMaster auto
    ControlPath ~/.ssh/cm_socket/%r@%h:%p
    # 配置为: yes 会话不会过期
    ControlPersist 600

# ssh登录: ssh user@hostname
# 会在 ~/.ssh/cm_socket 目录下生成对应的 user@hostname:port 会话

# 移除会话并释放相关资源: ssh -O exit user@hostname
```
