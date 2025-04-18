#!/bin/bash

# screen 基本用法

echo "
    screen -S name            # 创建会话
    screen -ls                # 列出会话
    screen -r name            # 恢复会话
    screen -d name            # 如果不能恢复,使用此命令后再screen -r name
    screen -S name -X quit    # 删除会话
    screen -d                 # 在当前会话中使用该命令,可以让当前会话挂起(detach status)
"