#!/usr/bin/env bash

## 这个脚本用于操作redis,有以下功能:
## 1. 匹配以prefix开头的key
## 2. 匹配以prefix结尾的key
## 3. 对于匹配出来的的key可以执行的动作：查看|删除
## 脚本参数:
## --address  redis地址
## --port     redis端口
## --password redis密码
## --prefix   匹配的key前缀
## --suffix   匹配的key后缀
## --db       redis数据库
## --action   执行的动作，可选值：view|delete
## --help     显示帮助信息

# 显示帮助信息
show_help() {
    cat << EOF
使用方法: $(basename "$0") [选项]

选项:
    --help      显示此帮助信息
    --address   Redis服务器地址 (默认: 127.0.0.1)
    --port      Redis端口 (默认: 6379)
    --password  Redis密码 (可选)
    --db        Redis数据库编号 (默认: 0)
    --prefix    键名前缀匹配
    --suffix    键名后缀匹配
    --action    执行的操作 [view|delete] (默认: view)

示例:
    # 查看以 "user:" 开头的键
    $(basename "$0") --prefix "user:" --action view

    # 删除以 "_temp" 结尾的键
    $(basename "$0") --suffix "_temp" --action delete

    # 在指定的 Redis 实例上操作
    $(basename "$0") --address 192.168.1.100 --port 6379 --password mypass --db 1 --prefix "cache:" --action delete
EOF
    exit 0
}

# 默认参数
REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DB="0"
KEY_PREFIX=""
KEY_SUFFIX=""
ACTION="view"
BATCH_SIZE=100

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --help)
            show_help
            ;;
        --address)
            REDIS_HOST="$2"
            shift 2
            ;;
        --port)
            REDIS_PORT="$2"
            shift 2
            ;;
        --password)
            REDIS_PASSWORD="$2"
            shift 2
            ;;
        --prefix)
            KEY_PREFIX="$2"
            shift 2
            ;;
        --suffix)
            KEY_SUFFIX="$2"
            shift 2
            ;;
        --db)
            REDIS_DB="$2"
            shift 2
            ;;
        --action)
            ACTION="$2"
            shift 2
            ;;
        *)
            echo "未知参数: $1"
            exit 1
            ;;
    esac
done

# 构建 redis-cli 基础命令
REDIS_CMD="redis-cli -h $REDIS_HOST -p $REDIS_PORT"
if [ ! -z "$REDIS_PASSWORD" ]; then
    REDIS_CMD="$REDIS_CMD -a $REDIS_PASSWORD"
fi
REDIS_CMD="$REDIS_CMD -n $REDIS_DB"

# 构建匹配模式
if [ ! -z "$KEY_PREFIX" ] && [ ! -z "$KEY_SUFFIX" ]; then
    MATCH_PATTERN="${KEY_PREFIX}*${KEY_SUFFIX}"
elif [ ! -z "$KEY_PREFIX" ]; then
    MATCH_PATTERN="${KEY_PREFIX}*"
elif [ ! -z "$KEY_SUFFIX" ]; then
    MATCH_PATTERN="*${KEY_SUFFIX}"
else
    # echo "错误：必须指定 --prefix 或 --suffix 参数"
    show_help
    exit 1
fi

# 使用 SCAN 命令遍历键
cursor=0
matched_keys=()
count=0

echo "开始扫描匹配的键..."
while true; do
    # 执行 SCAN 命令
    result=$($REDIS_CMD SCAN $cursor MATCH "$MATCH_PATTERN" COUNT $BATCH_SIZE)
    new_cursor=$(echo "$result" | head -n 1)
    keys=$(echo "$result" | tail -n +2)
    
    # 处理匹配到的键
    if [ ! -z "$keys" ]; then
        while read -r key; do
            if [ ! -z "$key" ]; then
                if [ "$ACTION" = "view" ]; then
                    echo "找到键: $key"
                    $REDIS_CMD TYPE "$key"
                elif [ "$ACTION" = "delete" ]; then
                    echo "删除键: $key"
                    $REDIS_CMD DEL "$key"
                fi
                ((count++))
            fi
        done <<< "$keys"
    fi
    
    # 添加短暂延时，避免对 Redis 造成过大压力
    sleep 0.1
    
    # 如果 cursor 为 0，说明遍历完成
    if [ "$new_cursor" = "0" ]; then
        break
    fi
    cursor=$new_cursor
done

echo "操作完成，共处理 $count 个键"
