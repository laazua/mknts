#!/bin/bash

## install bc.x86_64
## 先手动安装openvpn和easyrsa工具

set -e

export PATH=$PATH:/usr/local/bin

EASYRSA_DIR="/etc/openvpnooo/easy-rsa"
OUTPUT_DIR="/etc/openvpnooo/client-configs"
SERVER_CN="server"
SERVER_CONF="/etc/openvpnooo/server.conf"
PORT=1194
PROTO=udp
VPN_NETWORK="10.8.0.0"
VPN_NETMASK="255.255.255.0"
SERVER_NAME="myvpn"
DEFAULT_USER=${1:-client1}  # 支持通过参数传用户名


# 安装必要工具
install_packages() {
    apt update && apt install -y openvpn zip
}

# 初始化 PKI 环境
init_pki() {
    mkdir -p "$EASYRSA_DIR"
    cd "$EASYRSA_DIR"
    easyrsa init-pki
    echo -ne "\n\n" | easyrsa build-ca nopass
    easyrsa gen-dh
    easyrsa build-server-full "$SERVER_CN" nopass
    openvpn --genkey --secret ta.key
}

# 创建客户端证书
generate_client_cert() {
    local CLIENT_NAME=$1
    cd "$EASYRSA_DIR"
    easyrsa build-client-full "$CLIENT_NAME" nopass
}

# 生成服务端配置
generate_server_conf() {
    cat > "$SERVER_CONF" <<EOF
port $PORT
proto $PROTO
dev tun
ca $EASYRSA_DIR/pki/ca.crt
cert $EASYRSA_DIR/pki/issued/$SERVER_CN.crt
key $EASYRSA_DIR/pki/private/$SERVER_CN.key
dh $EASYRSA_DIR/pki/dh.pem
auth SHA256
tls-auth $EASYRSA_DIR/ta.key 0
cipher AES-256-CBC

topology subnet
server $VPN_NETWORK $VPN_NETMASK
ifconfig-pool-persist /var/log/openvpn/ipp.txt
keepalive 10 120
persist-key
persist-tun

status /var/log/openvpn/openvpn-status.log
log-append /var/log/openvpn/openvpn.log
verb 3
explicit-exit-notify 1
EOF
}

# 生成 .ovpn 客户端配置文件
generate_client_ovpn() {
    local CLIENT_NAME=$1
    local CLIENT_DIR="$OUTPUT_DIR/$CLIENT_NAME"
    mkdir -p "$CLIENT_DIR"

    cat > "$CLIENT_DIR/$CLIENT_NAME.ovpn" <<EOF
client
dev tun
proto $PROTO
remote YOUR_SERVER_IP $PORT
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth SHA256
cipher AES-256-CBC
verb 3
<ca>
$(cat $EASYRSA_DIR/pki/ca.crt)
</ca>
<cert>
$(cat $EASYRSA_DIR/pki/issued/$CLIENT_NAME.crt)
</cert>
<key>
$(cat $EASYRSA_DIR/pki/private/$CLIENT_NAME.key)
</key>
<tls-auth>
$(cat $EASYRSA_DIR/ta.key)
</tls-auth>
key-direction 1
EOF
    echo "[+] 生成完成：$CLIENT_DIR/$CLIENT_NAME.ovpn"
}

# 启动 OpenVPN 服务
start_openvpn() {
    systemctl enable openvpn@server
    systemctl start openvpn@server
    systemctl status openvpn@server --no-pager
}

# 主流程
main() {
#    install_packages
    init_pki
    generate_client_cert "$DEFAULT_USER"
    generate_server_conf
    generate_client_ovpn "$DEFAULT_USER"
#    start_openvpn
}

main "$@"

