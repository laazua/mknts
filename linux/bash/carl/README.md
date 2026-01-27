### carl

- 描述:
    carl: ca remote login

- 说明:
    1. ssh ca证书认证登录远程主机
    2. carl 为CA服务, 提供证书颁发，管理等
    3. carlctl 为客户端命令行工具, 部署在自己的节点上

- 流程：
    1. CA服务器: mkdir -p /etc/ssh/ca/user_rsa_pub
    1. CA服务器创建ca公钥和私钥: ssh-keygen -t rsa -b 4096 -f /etc/ssh/ca/ca -C "SSH User CA"
    2. 将CA公钥传递到被登录服务`注: 业务主机`(并进行相关sshd配置,重启sshd)
        1. 业务主机: mkdir -p /etc/ssh/ca
        2. CA服务器: scp ca.pub 业务主机:/etc/ssh/ca/user_key.pub
        3. 业务主机: cat /etc/ssh/sshd_config.d/10-zhangsan.conf
        ```bash
        # 信任用户CA
        TrustedUserCAKeys /etc/ssh/ca/user_key.pub

        # 信任主机CA（可选，增强安全性）
        #HostCertificate /etc/ssh/ssh_host_rsa_key-cert.pub

        # 禁用密码认证（生产环境推荐）
        PasswordAuthentication no
        ChallengeResponseAuthentication no
        UsePAM no

        # 允许证书认证
        PubkeyAuthentication yes
        AuthorizedKeysFile .ssh/authorized_keys

        # 日志级别
        LogLevel VERBOSE

        # 证书相关选项
        # 允许用户证书中的命令强制执行
        PermitUserRC yes
        ```
    3. 登录服务器`注: 堡垒机`生成用户密钥(并将用户公钥用户CA服务器的CA私钥进行签名,然后回传到登录服务器进行配置):
        1. 堡垒机: ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_ca -C "user-cert"
        2. 堡垒机: scp ~/.ssh/id_rsa_ca.pub CA服务器:/etc/ssh/ca/user_rsa_pub/zhangsan_id_rsa_ca.pub
        3. CA服务器: ssh-keygen -s /etc/ssh/ca/ca -I "user_$(date +%Y%m%d)" -n "zhangsan" -V +30d -z $(date +%Y%m%d%H%M%S) /etc/ssh/ca/user_rsa_pub/zhangsan_id_rsa_ca.pub
        4. CA服务器: scp /etc/ssh/ca/user_rsa_pub/zhangsan_rsa_ca-cert.pub 堡垒机:~/.ssh/id_rsa_ca-cert.pub
        5. 堡垒机用户登录ssh配置: cat ~/.ssh/config
        ```bash
        Host 192.168.165.73
            HostName 192.168.165.73
            User zhangsan
            IdentityFile ~/.ssh/id_rsa_ca
            CertificateFile ~/.ssh/id_rsa_ca-cert.pub
        ```
        6. 堡垒机进行登录测试
- 撤销认证
    + KRL（Key Revocation List）文件方式:
        1. KRL=/etc/ssh/ca/revoked.krl
        2. CA服务器: SERIALID=$(ssh-keygen -L -f /etc/ssh/ca/user_rsa_pub/zhangsan_rsa_ca-cert.pub | grep Serial|awk -F: '{print $2}')
        3. CA服务器: ssh-keygen -k -u -f $KRL -z ${SERIALID}
        4. CA服务器: 同步KRL: scp ${KPL} 业务主机:${KRL}
        5. 业务服务器: 配置sshd: echo "RevokedKeys /etc/ssh/ca/revoked.krl" >> /etc/ssh/sshd_config.d/10-zhangsan.conf; 重启sshd
    + 基于文件的撤销列表(RevokedKeys):
        1. CA服务器: echo "serial: $(ssh-keygen -L -f /etc/ssh/ca/user_rsa_pub/zhangsan_rsa_ca-cert.pub | grep Serial | awk '{print $2}')" >> /etc/ssh/ca/revoked_keys
        2. CA服务器: 同步revoked_keys: scp /etc/ssh/ca/revoked_keys 业务主机:/etc/ssh/ca/revoked_keys
        3. 业务主机: 配置sshd: echo "RevokedKeys /etc/ssh/ca/revoked_keys" > /etc/ssh/sshd_config.d/10-zhangsan.conf; 重启sshd
