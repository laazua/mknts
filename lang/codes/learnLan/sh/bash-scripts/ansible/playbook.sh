#!/bin/bash

# playbook组件包括的内容:
# target: 定义playbook的远程主机组
#         target常用参数:
#         hosts: 定义远程主机组
#         user: 执行改任务的用户
#         sudo: 设置为yes的时候,执行任务的时候使用root权限
#         sudo_user: 指定sudo普通用户
#         connection: 默认基于ssh连接客户端
#         gather_facks: 获取远程主机facts基础信息

# variable: 定义playbook使用的变量
#         variable常用参数:
#         vars: 定义变量, 格式: 变量名:变量值
#         vars_files: 指定变量文件
#         vars_prompt: 用户交互模式自定义变量
#         setup: 模块取远程主机上的值

# task: 定义远程主机上执行的任务列表
#         task常用参数:
#         name: 任务显示名称,即屏幕显示信息
#         action: 定义执行的动作
#         copy: 复制本地文件到远程主机
#         template: 复制本地文件到远程主机,可以引用本地变量
#         service: 定义服务的状态
#         notify: 定义handler事件列表

# handler: 定义task执行完成以后需要调用的任务,例如配置文件被改动后,则启动handler任务重启关联的服务
