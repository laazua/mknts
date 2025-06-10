##### 说明:
#####   1. 将此配置添加在/etc/profile.d/usercmd.sh中
#####   2. root权限执行: source /etc/profile.d/usercmd.sh

# 用户操作历史记录配置
USER_IP=$(who -u am i 2>/dev/null | awk '{print $NF}' | sed -e 's/[()]//g')
if [ -z "$USER_IP" ]; then
    USER_IP=$(hostname)
fi

# 设置历史日志目录
HISTDIR=/usr/local/.usercmd
if [ ! -d "$HISTDIR" ]; then
    mkdir -p "$HISTDIR"
    chmod 777 "$HISTDIR"
fi

# 保持history命令默认输出不变
export HISTSIZE=20
export HISTFILESIZE=40

# 使用PROMPT_COMMAND记录详细日志但不影响history输出
export PROMPT_COMMAND='CMD=$(history 1 | { read -r _ cmd; echo "$cmd"; });echo "$(date "+%F %T") [$(whoami)] [${USER_IP}] $CMD" >> "$HISTDIR/$(whoami)-history-$(date +%Y-%m-%d).log"'
