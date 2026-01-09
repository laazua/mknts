// 脚本模板

package cmds

import (
	"fmt"

	"camassh/internal/config"
)

var (
	// 初始化目录脚本
	initCaScript = fmt.Sprintf(`#!/usr/bin/env bash
set -e

# 1. 创建 SSH CA 目录结构
mkdir -p %[1]s/{users,hosts}/{certs,private,public,crl}
mkdir -p %[1]s/templates
mkdir -p %[1]s/bin

# 2. 设置严格权限
chmod 700 %[1]s/users/private
chmod 700 %[1]s/hosts/private
chmod 755 %[1]s/{users,hosts}/{certs,public,crl}
chown -R root.root %[1]s/

# 3. 创建 CA 根密钥对
# 进入 CA 目录
cd %[1]s

# 1. 创建用户 CA 密钥对（用于验证用户身份）
ssh-keygen -t rsa -b 4096 \
-f users/private/user-ca \
-C "SSH User Certificate Authority" \
-N ""  # 不设置密码（生产环境建议设置）

# 2. 创建主机 CA 密钥对（可选，用于验证服务器身份）
ssh-keygen -t rsa -b 4096 \
-f hosts/private/host-ca \
-C "SSH Host Certificate Authority" \
-N ""

# 3. 将公钥复制到公共目录
cp users/private/user-ca.pub users/public/
cp hosts/private/host-ca.pub hosts/public/

# 4. 查看生成的密钥
echo "=== 用户 CA 公钥 ==="
cat users/public/user-ca.pub
echo -e "\n=== 主机 CA 公钥 ==="
cat hosts/public/host-ca.pub

# 5. 记录公钥指纹（重要！）
ssh-keygen -lf users/private/user-ca
ssh-keygen -lf hosts/private/host-ca
`, config.Get().CA().Path())
	// 用户证书签发脚本
	issueUserCertScript = fmt.Sprintf(`cat >%[1]s/bin/issue-user-cert.sh<<'EOF'
#!/bin/bash
# SSH 用户证书签发脚本
# 用法: issue-user-cert.sh <用户名> [有效期天数] [权限选项]

set -e

# 配置文件
CA_KEY="%[1]s/users/private/user-ca"
CERT_DIR="%[1]s/users/certs"
LOG_DIR="%[2]s"
LOG_FILE="$LOG_DIR/user-certs.log"

NETS_TMP="%[3]s"

# 创建日志目录
mkdir -p "$LOG_DIR"
touch "$LOG_FILE"

# 参数检查
if [ $# -lt 1 ]; then
    echo "错误: 缺少参数"
    echo "用法: $0 <用户名> [有效期天数] [权限选项]"
    echo "示例: $0 alice 30 'no-port-forwarding,no-x11-forwarding'"
    exit 1
fi

USERNAME="$1"
VALIDITY_DAYS="${2:-30}"  # 默认30天
OPTIONS="${3:-}"
PRINCIPALS="$USERNAME,admin"  # 允许登录的用户名（可登录为多个用户）

# 用户公钥文件（假设从客户端上传）
USER_PUB_KEY="/tmp/${USERNAME}-ssh-pubkey-$(date +%%s).pub"

echo "请将用户的公钥内容粘贴到下面 (以 ssh-rsa/ssh-ed25519 开头，以用户邮箱或注释结尾)"
echo "粘贴完成后按 Ctrl+D"
cat > "$USER_PUB_KEY"

# 验证公钥格式
if ! ssh-keygen -l -f "$USER_PUB_KEY" &>/dev/null; then
    echo "错误: 无效的公钥格式"
    rm -f "$USER_PUB_KEY"
    exit 1
fi

# 生成唯一证书ID
CERT_ID="${USERNAME}-$(date +%%Y%%m%%d-%%H%%M%%S)"
CERT_FILE="${CERT_DIR}/${CERT_ID}.pub"

# 计算有效期
VALIDITY="+${VALIDITY_DAYS}d"

# 构建签发命令
SIGN_CMD="ssh-keygen -s \"$CA_KEY\" -I \"$CERT_ID\" -n \"$PRINCIPALS\" -V \"$VALIDITY\""

# 添加额外选项
if [ -n "$OPTIONS" ]; then
    # 解析选项并添加到命令
    IFS=',' read -ra OPTS <<< "$OPTIONS"
    for opt in "${OPTS[@]}"; do
        SIGN_CMD="$SIGN_CMD -O $opt"
    done
fi

# 添加源地址限制（示例：仅允许从特定网络访问）
NETS_ADDR=""
NETS=$(echo "$NETS_TMP" | tr '[' ' '| tr ']' ' ')
for netIp in ${NETS[@]};do
  NETS_ADDR="$NETS_ADDR -O source-address=\"${netIp}\""
done
SIGN_CMD="$SIGN_CMD $NETS_ADDR"
echo "XXXXX =>" $SIGN_CMD

# 完成命令
SIGN_CMD="$SIGN_CMD \"$USER_PUB_KEY\""

echo "正在签发证书..."
eval "$SIGN_CMD"

# 移动证书到存储目录
PUB_KEY_NAME=$(echo ${USER_PUB_KEY}|awk -F'.' '{print $1}')
mv "${PUB_KEY_NAME}-cert.pub" "$CERT_FILE"

# 清理临时文件
rm -f "$USER_PUB_KEY"

# 记录日志
echo "$(date '+%%Y-%%m-%%d %%H:%%M:%%S') - 用户: $USERNAME - 证书: $CERT_ID - 有效期: $VALIDITY_DAYS天" >> "$LOG_FILE"

echo ""
echo "========== 证书签发成功 =========="
echo "证书文件: $CERT_FILE"
echo "证书ID: $CERT_ID"
echo "有效期: $VALIDITY_DAYS 天"
echo "允许的用户: $PRINCIPALS"
echo "=================================="
echo ""
echo "请将以下证书内容发送给用户:"
cat "$CERT_FILE"
EOF`, config.Get().CA().Path(), config.Get().CA().LogPath(), config.Get().CA().Nets())

	// 主机证书签发脚本
	issueHostCertScript = fmt.Sprintf(`cat >%[1]s/bin/issue-host-cert.sh<<'EOF'
cat > /etc/ssh-ca/bin/issue-host-cert.sh << 'EOF'
#!/bin/bash
# SSH 主机证书签发脚本

set -e

CA_KEY="%[1]s/hosts/private/host-ca"
CERT_DIR="%[1]s/hosts/certs"
HOSTNAME="$1"

if [ -z "$HOSTNAME" ]; then
    echo "用法: $0 <主机名或IP>"
    exit 1
fi

# 从目标服务器获取主机公钥（需要提前配置SSH密钥登录）
echo "正在从 $HOSTNAME 获取主机公钥..."
scp root@$HOSTNAME:/etc/ssh/ssh_host_rsa_key.pub /tmp/host-key-${HOSTNAME}.pub 2>/dev/null || {
    echo "无法获取主机公钥，请手动提供"
    exit 1
}

HOST_PUB_KEY="/tmp/host-key-${HOSTNAME}.pub"

# 签发主机证书（有效期为2年）
ssh-keygen -s "$CA_KEY" \
    -I "host-${HOSTNAME}-$(date +%%Y%%m%%d)" \
    -h \  # 重要：标记为主机证书
    -n "$HOSTNAME, $(dig +short $HOSTNAME | tr '\n' ',')" \
    -V "-1w:+104w" \  # 一周前生效，104周后过期
    "$HOST_PUB_KEY"

# 移动证书
mv "${HOST_PUB_KEY}-cert.pub" "${CERT_DIR}/host-${HOSTNAME}.pub"

# 将证书发送回目标服务器
scp "${CERT_DIR}/host-${HOSTNAME}.pub" root@$HOSTNAME:/etc/ssh/ssh_host_rsa_key-cert.pub

echo "主机证书已签发并部署到 $HOSTNAME"
EOF

chmod +x %[1]s/bin/issue-host-cert.sh`, config.Get().CA().Path())
	// 吊销证书脚本
	revokeCertScript = fmt.Sprintf(`cat >%[1]s/bin/revoke-cert.sh<<'EOF'
cat > /etc/ssh-ca/bin/revoke-cert.sh << 'EOF'
#!/bin/bash
# SSH 证书吊销脚本

set -e

CRL_FILE="%[1]s/users/crl"
CA_KEY="%[1]s/users/private/user-ca"

if [ $# -lt 1 ]; then
    echo "用法: $0 <证书文件或公钥文件> [原因]"
    exit 1
fi

CERT_FILE="$1"
REASON="${2:-revoked-by-admin}"

# 如果提供的是证书文件，提取其中的公钥
if [[ "$CERT_FILE" == *-cert.pub ]]; then
    # 从证书中提取公钥
    TMP_PUBKEY="/tmp/pubkey-$(basename $CERT_FILE)"
    ssh-keygen -L -f "$CERT_FILE" | grep -A1 "Public key" | tail -1 | sed 's/^ *//' > "$TMP_PUBKEY"
    KEY_TO_REVOKE="$TMP_PUBKEY"
else
    KEY_TO_REVOKE="$CERT_FILE"
fi

# 添加到吊销列表
if [ ! -f "$CRL_FILE" ]; then
    ssh-keygen -k -f "$CRL_FILE"
fi

ssh-keygen -u -f "$CRL_FILE" -s "$CA_KEY" -z "1" "$KEY_TO_REVOKE"

# 清理临时文件
[ -f "$TMP_PUBKEY" ] && rm -f "$TMP_PUBKEY"

echo "证书已吊销"
echo "请将吊销列表 $CRL_FILE 分发到所有服务器"
EOF

chmod +x %[1]s/bin/revoke-cert.sh`, config.Get().CA().Path())
	// 准备分发脚本
	distributeCaPubKeyScript = fmt.Sprintf(`cat >%[1]s/bin/distribute-ca-pubkey.sh<<'EOF'
#!/bin/bash
# 分发 CA 公钥到目标服务器

set -e

USER_CA_PUB="%[1]s/users/public/user-ca.pub"
HOST_CA_PUB="%[1]s/hosts/public/host-ca.pub"

# 目标服务器列表
SERVERS=$1  # 只需要目标服务器信任CA $1="127.0.0.1 192.168.165.73"

for SERVER in "${SERVERS[@]}"; do
    echo "分发到 $SERVER..."
    
    # 分发用户 CA 公钥
    scp "$USER_CA_PUB" root@$SERVER:/etc/ssh/user-ca.pub
    
    # 在目标服务器上配置信任CA
    ssh root@$SERVER << 'REMOTE_EOF'
        # 确保 SSH 目录存在
        mkdir -p /etc/ssh
        
        # 备份原始配置
        cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%%Y%%m%%d)
        
        # 检查是否已配置 TrustedUserCAKeys
        if ! grep -q "TrustedUserCAKeys" /etc/ssh/sshd_config; then
            echo "TrustedUserCAKeys /etc/ssh/user-ca.pub" >> /etc/ssh/sshd_config
        else
            sed -i 's|^TrustedUserCAKeys.*|TrustedUserCAKeys /etc/ssh/user-ca.pub|' /etc/ssh/sshd_config
        fi
        
        # 确保权限正确
        chmod 644 /etc/ssh/user-ca.pub
        chown root:root /etc/ssh/user-ca.pub
        
        # 重启 SSH 服务
        systemctl restart sshd
        echo "已为 $SERVER 配置信任 CA"
REMOTE_EOF
    
    echo "完成 $SERVER"
done

echo "所有服务器配置完成"
EOF
chmod +x %[1]s/bin/distribute-ca-pubkey.sh`, config.Get().CA().Path())
)
