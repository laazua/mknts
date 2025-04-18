#!/bin/bash

# k8s基础知识

# 二进制部署: https://www.cnblogs.com/noah-luo/p/13345164.html

echo "
    容器资源管理: mesos(淘汰), docekr swarm(docker官方), k8s(推荐)
    建议参考官网进行学习

    ## k8s简介
    前身borg系统,用go语言重写 
                                              kubectl
             # # # # # # # # # # # # # # # # /
             #        scheduler            #              
	     #	              \          / #
	     #    	       api server<-# --> etcd(键值对数据库)
             #                /          \ #
             # replication controller      #             
             # # # # # # # # # # # # # # # # \
                 internet                     web UI
                    |firewall
               # # # # # # #  kubelet
	node:  # Pod1 Pod2 #  kube proxy 
	       # # # # # # #

        Pod: container1 container2 ... 共享网络,卷

     ## 重要组件
     api server: 所有服务的统一访问入口
     crontrollerManager: 维持副本期望树木
     scheduler: 负责任务调度,选择合适的节点进行任务分配
     etcd: 键值对数据库,存储k8s集群所有重要信息
     kebelet: 直接跟容器引擎交互实现容器生命的周期管理
     kube-proxy: 负责写入规则至iptables,IPVS实现服务映射访问

     coredns:可以为集群中的svc创建一个域名IP的对应关系解析
     dashboard: 给k8s集群提供一个b/s结构的访问体系
     ingress controller: 可以实现7层代理
     fedetation: 提供一个可以跨集群中心多k8s统一管理功能
     prometheus: 给k8s集群提供一个监控
     kle: 提供k8s集群日志统一分析介入平台
	
    ## Pod
        自主式Pod: 死亡后不能从副本恢复
	控制器管理式Pod:

    ## 网络通讯方式
	
	
	
	
	
"
