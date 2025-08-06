### openVpn

- openvpn版本
```text
OpenVPN 2.7-0.20250326gitd167815.el10_0 x86_64-redhat-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
library versions: OpenSSL 3.2.2 4 Jun 2024, LZO 2.10
DCO version: N/A
Originally developed by James Yonan
Copyright (C) 2002-2024 OpenVPN Inc <sales@openvpn.net>
Compile time defines: enable_async_push=yes enable_comp_stub=no enable_crypto_ofb_cfb=yes enable_dco=auto enable_dco_arg=auto enable_debug=yes enable_dependency_tracking=no enable_dlopen=unknown enable_dlopen_self=unknown enable_dlopen_self_static=unknown enable_fast_install=yes enable_fragment=yes enable_iproute2=no enable_libtool_lock=yes enable_lz4=yes enable_lzo=yes enable_management=yes enable_ntlm=yes enable_pam_dlopen=no enable_pedantic=no enable_pkcs11=yes enable_plugin_auth_pam=yes enable_plugin_down_root=yes enable_plugins=yes enable_port_share=yes enable_selinux=yes enable_shared=yes enable_shared_with_static_runtimes=no enable_silent_rules=yes enable_small=no enable_static=yes enable_strict=no enable_strict_options=no enable_systemd=yes enable_werror=no enable_win32_dll=yes enable_wolfssl_options_h=yes enable_x509_alt_username=yes with_aix_soname=aix with_crypto_library=openssl with_gnu_ld=yes with_mem_check=no with_openssl_engine=auto with_sysroot=no
```

- 环境准备(三台rocky linux主机)
1. 192.168.165.83  (server)
2. 192.168.165.84  (client)
3. 192.168.165.85  (client)


- 三台主机都执行一下命令
1. sudo dnf install -y epel-release
2. sudo dnf install -y openvpn

- 生成证书
```bash
# 安装easyrsa工具(从openvpn的github下载直接解压,然后将可执行文件easyrsa移动到/usr/local/bin路径)
tar -xzf EasyRSA-git-development.tgz && sudo mv EasyRSA-git-development/easyrsa /usr/local/bin/
# 生成服务端和客户端证书
mkdir certs && cd certs
easyrsa init-pki
easyrsa build-ca nopass
# 生成服务端证书
easyrsa gen-req server nopass
easyrsa sign-req server server
# 生成客户端证书(节点1)
easyrsa gen-req client1 nopass
easyrsa sign-req client client1
# 生成客户端证书(节点2)
easyrsa gen-req client2 nopass
easyrsa sign-req client client2
easyrsa gen-dh
penvpn --genkey --secret ta.key
```

- 解压docs目录下的配置压缩文件到指定的目录下
1. tar -xzf openvpn-server.tar.gz -C /etc/openvpn   (服务端)
2. tar -xzf openvpn-client.tar.gz -C /etc/openvpn   (客户端)
3. 修改服务端和配置端的相关配置(IP地址和相关证书证书)

- openvpn启动
1. 服务端: openvpn --config /etc/openvpn/server/server.conf
2. 客户端: openvpn --config /etc/openvpn/client/client.conf

- 配置防火墙安全规则
```txt
1. 允许vpn所在服务器进行外网访问
   a. 系统内核参数配置:  
      echo "net.ipv4.ip_forward=1" >>/etc/sysctl.conf && sysctl -p
   b. 允许网络转发: 
        firewall-cmd --permanent --add-masquerade
        firewall-cmd --permanent --direct --add-rule ipv4 nat POSTROUTING 0 -s 10.8.0.0/24 -o eth0 -j MASQUERADE
        firewall-cmd --reload
      或者：
        iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE  # -s参数为vpn虚拟网段

2. 配置openvpn服务器与各个客户端节点服务的防火墙访问规则(最小权限原则)
```

- 使用unbound软件服务进行vpn虚拟网段中的域名解析

