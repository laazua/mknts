#!/bin/bash

CMD="/usr/bin/firewall-cmd"
ZONE_NAME="tmpz"
INTERFACE="ens192"          # 替换为你的实际网卡名
WHITELIST_IPS=("192.168.1.100" "192.168.165.88")  # 你允许访问的 IP

# 创建自定义 zone（如果不存在）
if ! $CMD --get-zones | grep -qw "$ZONE_NAME"; then
    echo "创建 zone: $ZONE_NAME"
    $CMD --permanent --new-zone=$ZONE_NAME
fi

# 清空 zone 的所有现有规则（确保纯净）
echo "清空 zone: $ZONE_NAME 的所有规则"
RICH_RULES=$($CMD --permanent --list-rich-rules --zone $ZONE_NAME)
if [[ -n "$RICH_RULES" ]]; then
    echo "清除已有 rich-rules:"
    while IFS= read -r rule; do
        echo "删除规则: $rule"
        $CMD --permanent --zone=$ZONE_NAME --remove-rich-rule="$rule"
    done <<< "$RICH_RULES"
else
    echo "没有需要删除的 rich-rule"
fi
$CMD --permanent --zone=$ZONE_NAME --remove-interface=$INTERFACE

# 添加 rich-rule 白名单 IP
for ip in "${WHITELIST_IPS[@]}"; do
    echo "添加白名单 IP: $ip"
    $CMD --permanent --zone=$ZONE_NAME \
        --add-rich-rule="rule family='ipv4' source address='$ip' accept"
done

# 默认拒绝其他访问
echo "设置默认策略为拒绝"
$CMD --permanent --zone=$ZONE_NAME --set-target=DROP

# 绑定网卡到新 zone
echo "绑定网卡 $INTERFACE 到 zone $ZONE_NAME"
$CMD --permanent --zone=$ZONE_NAME --add-interface=$INTERFACE

# 应用更改
echo "重新加载 firewalld"
$CMD --reload

# 验证
echo "验证规则"
$CMD --zone=$ZONE_NAME --list-all

