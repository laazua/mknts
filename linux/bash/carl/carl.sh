#!/bin/bash

## Linux ssh CA 认证登录
## CA 服务器运行此脚本进行相关初始化操作

set -e

# 加载环境变量
ENV_FILE=".env"
if [[ -f "${ENV_FILE}" ]];then
  source "${ENV_FILE}"
fi

# 颜色变量
RED='\033[0;31m'
GREEN='\033[0;32m'
RESET='\033[0m'
function _red() {
  echo -e "${RED}$1${RESET}"
}

function _green() {
  echo -e "${GREEN}$1${RESET}"
}

function main() {
  local ACTION=""
  
  while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
        _help
        ;;
        -a|--action)
        # 检查是否有下一个参数
        if [[ -z "$2" ]] || [[ "$2" =~ ^- ]]; then
            echo "错误：-a/--action 需要一个参数"
            _help
        fi
        ACTION="$2"
        shift 2  # 消耗两个参数：-a 和它的值
        ;;
        -*)
        echo "未知选项: $1"
        exit 1
        ;;
        *)
        # 非选项参数
        shift
        ;;
    esac
  done

  read -p "config file ssh.conf and 10-ca-auth.conf is ready?[y|n]: " ENTER
  if [ "${ENTER}" != "y" ];then
    echo "Please config file ssh.conf and 10-ca-auth.conf"
    exit
  fi

  [ -z "${ACTION}" ] && _help
  check_env "${ENV_FILE}"
  init_ca
  
  case "${ACTION}" in
    "add-user")
      init_clt
      ;;
    "del-user")
      revoke_ca
      ;;
    "init-node")
      init_srv
      ;;
    *)
      echo "未知的操作: ${ACTION}"
      _help
      ;;
  esac
}

function check_env() {
  # 检测相关命令
  if ! command -v ssh-keygen >/dev/null; then
    echo "Please install: openssh openssh-server openssh-clients openssl"
    exit 1
  fi
  if ! command -v scp >/dev/null; then
    echo "scp command is required"
    exit 1
  fi
  
  source "$1"
  # 检测.env配置
  : "${CA_PATH:?CA_PATH environment variable is required}"
  : "${CA_DESC:-'SSH CA AUTH'}"
  : "${CA_EXPIRED:-'365d'}"
  : "${SRV_CA_PATH:?SRV_CA_PATH environment variable is required}"
  : "${CLT_ADDR:?CLT_ADDR environment variable is required}"
  : "${CLT_PORT:-'22'}"
}

## CA服务器初始化
function init_ca() {
  if [ ! -d "${CA_PATH}" ];then
    mkdir -p "${CA_PATH}/user_rsa_pub"
  fi
  # 初始化CA密钥
  if [ ! -f "${CA_PATH}/ca.pub" ];then
    ssh-keygen -t rsa -b 4096 -f "${CA_PATH}/ca" -C "${CA_DESC}"
  fi
}

## 客户端初始化
function init_clt() {
  read -p "Please Input SSH CA Auth Login UserName: " USERNAME
  if [ -z "${USERNAME}" ];then
    echo "Please Input CA Auth Login UserName"
    exit 1
  fi
  
  # 在客户端创建用户
  _green "add user: ${USERNAME}, Please input ROOT login passwd and set ${USERNAME}'s passwd!"
  ssh -p "${CLT_PORT}" "root"@"${CLT_ADDR}" "groupadd ${USERNAME} && adduser -m -g ${USERNAME} ${USERNAME} && passwd ${USERNAME}"
  
  # 生成用户密钥
  _green "gen user cert, Please input ${USERNAME} login passwd ..."
  ssh -p "${CLT_PORT}" "${USERNAME}"@"${CLT_ADDR}" "mkdir -p ~/.ssh && ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_ca -N '' -C user-cert"
  
  # 将用户公钥拷贝到CA服务
  _green "scp user pub key to CA server, Please input ${USERNAME} login passwd ..."
  scp -P "${CLT_PORT}" "${USERNAME}@${CLT_ADDR}:~/.ssh/id_rsa_ca.pub" "${CA_PATH}/user_rsa_pub/${USERNAME}_id_rsa_ca.pub"
  
  # 用CA证书给用户认证
  _green "auth user with CA pub key ..."
  ssh-keygen -s "${CA_PATH}/ca" -I "user_$(date +%Y%m%d)" -n "${USERNAME}" -V "+${CA_EXPIRED}" -z $(date +%Y%m%d%H%M%S) "${CA_PATH}/user_rsa_pub/${USERNAME}_id_rsa_ca.pub"
  
  # 将生成的用户证书拷贝回客户端
  _green "scp CA cert to client server, Please input ${USERNAME} login passwd ..."
  scp -P "${CLT_PORT}" "${CA_PATH}/user_rsa_pub/${USERNAME}_id_rsa_ca-cert.pub" "${USERNAME}@${CLT_ADDR}:~/.ssh/id_rsa_ca-cert.pub"
  
  # 用户登录配置
  _green "config user ssh info, Please input ${USERNAME} login passwd ..."
  if [ -f "ssh.conf" ]; then
    sed "s/TMPUSER/${USERNAME}/g" ssh.conf | ssh -p "${CLT_PORT}" "${USERNAME}"@"${CLT_ADDR}" "cat >~/.ssh/config"
    # scp -P "${CLT_PORT}" "ssh.conf" "${USERNAME}@${CLT_ADDR}:~/.ssh/config"
  else
    echo "警告: ssh.conf 文件不存在，跳过上传"
  fi
  
  echo "用户 ${USERNAME} 的CA认证已配置完成"
}

## 服务端初始化
function init_srv() {
  read -p "Please Input Server Address: " SRVADDR
  read -p "Please Input Server Port (default 22): " SRVPORT
  SRVADDR="${SRVADDR:-$SRVADDR}"
  SRVPORT="${SRVPORT:-22}"

  # 在服务端创建目录
  _green "create ssh ca path, Please input ROOT login passwd ..."
  ssh -p "${SRVPORT}" "root@${SRVADDR}" "[ ! -d ${SRV_CA_PATH} ] && mkdir -p ${SRV_CA_PATH} && touch ${SRV_CA_PATH}/revoked_keys"
  
  # 拷贝CA公钥到服务端
  _green "scp CA pub key to server, Please input ROOT login passwd ..."
  scp -P "${SRVPORT}" "${CA_PATH}/ca.pub" "root@${SRVADDR}:${SRV_CA_PATH}/ca.pub"
  
  # 上传sshd认证配置
  _green "scp sshd config to server, Please input ROOT login passwd ..."
  if [ -f "10-ca-auth.conf" ]; then
    scp -P "${SRVPORT}" "10-ca-auth.conf" "root@${SRVADDR}:/etc/ssh/sshd_config.d/10-ca-auth.conf"
  else
    echo "警告: 10-ca-auth.conf 文件不存在，请手动创建"
  fi
  
  # 重启sshd服务
  _green "restart sshd service, Please input ROOT login passwd ..."
  ssh -p "${SRVPORT}" "root@${SRVADDR}" "systemctl restart sshd"
  
  echo "服务器 ${SRVADDR}:${SRVPORT} 的CA认证已配置完成"
}

## 撤销用户CA认证
function revoke_ca() {
  read -p "Please Input Username to revoke: " USERNAME
  
  if [ -z "${USERNAME}" ]; then
    echo "Please Input Username"
    exit 1
  fi
  
  # 删除用户证书文件
  if [ -f "${CA_PATH}/user_rsa_pub/${USERNAME}_id_rsa_ca-cert.pub" ]; then
    rm -f "${CA_PATH}/user_rsa_pub/${USERNAME}_id_rsa_ca-cert.pub"
    echo "已删除用户 ${USERNAME} 的证书文件"
  fi
  
  # 从服务端移除用户授权（需要服务端实现撤销列表）
  echo "注意：需要在所有配置了CA认证的服务器上手动更新撤销列表"
  echo "可以在服务器上执行以下命令来拒绝特定用户："
  echo "在 /etc/ssh/sshd_config 或 /etc/ssh/sshd_config.d/10-ca-auth.conf 中添加："
  echo "RevokedKeys ${SRV_CA_PATH}/revoked_keys"
  echo "然后创建 ${SRV_CA_PATH}/revoked_keys 文件并添加用户的公钥指纹"
}

## 脚本帮助信息
function _help() {
  cat << EOF

使用方法: $0 [选项]

选项:
  -h, --help          显示此帮助信息
  -a, --action <动作>  指定要执行的动作
  
可用动作:
  add-user            添加CA认证用户
  del-user            撤销用户CA认证
  init-node           初始化服务器节点

示例:
  $0 -a add-user      添加一个CA认证用户
  $0 -a init-node     初始化服务器节点
  $0 -a del-user      撤销用户CA认证

环境变量配置:
  请确保 .env 文件包含以下变量:
  CA_PATH: CA证书存储路径
  CA_DESC: CA描述（可选）
  CA_EXPIRED: 证书有效期（可选，默认365d）
  SRV_CA_PATH: 服务端CA证书存储路径
  CLT_ADDR: 客户端地址
  CLT_PORT: 客户端SSH端口（可选，默认22）

EOF
  exit 0
}

main "$@"