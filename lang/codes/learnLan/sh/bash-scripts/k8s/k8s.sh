#!/bin/bash
:<<!
1. k8s是什么?
  kubernetes由一系列组件组成的一个集群,是管理容器应用的一个开源系统,可移植,可扩展.
  master(192.167.7.1):
    -- kube-apiserver
       负责处理来自用户的请求，其主要作用就是对外提供 RESTful 的接口，包括用于查看集群状态的读请求以及改变集群状态的写请求，也是唯一一个与 etcd 集群通信的组件
    -- kube-scheduler
       调度器其实为 Kubernetes 中运行的 Pod 选择部署的 Worker 节点，它会根据用户的需要选择最能满足请求的节点来运行 Pod，它会在每次需要调度 Pod 时执行
    -- kube-controller-manager
       管理器运行了一系列的控制器进程，这些进程会按照用户的期望状态在后台不断地调节整个集群中的对象，当服务的状态发生了改变，控制器就会发现这个改变并且开始向目标状态迁移
       cloud-controller-manager

  数据存储(192.168.7.2):
    -- etcd1, etcd2, etcd3...

  node集群:
    node1(安装docker引擎)(192.168.7.3):
      -- kubelet
         是一个节点上的主要服务，它周期性地从 API Server 接受新的或者修改的 Pod 规范并且保证节点上的 Pod 和其中容器的正常运行，还会保证节点会向目标状态迁移，该节点仍然会向 Master 节点发送宿主机的健康状况
      -- kube-proxy
         负责宿主机的子网管理，同时也能将服务暴露给外部，其原理就是在多个隔离的网络中把请求转发给正确的 Pod 或者容器
      -- docker
    node2(安装docker引擎)(192.168.7.4):
      -- kubelet
      -- kube-proxy
      -- docker
    node3(安装docker引擎)(192.168.7.5):
      ...

1. 安装环境要求(所有主机):
  -- centos7
       -- 关闭防火墙
          systemctl stop firewalld
          systemctl disable firewalld
       -- 关闭selinux
          sed -i "s/enforcing/disabled/" /etc/selinux/config
       -- 将桥接的ipv4流量传递到iptables的链
          cat /etc/sysctl.d/k8s.conf << EOF
              net.bridge.bridge-nf-call-ip6tables = 1
              net.bridge.bridge-nf-call-iptables = 1
              EOF
          sysctl --system
  -- RAM >= 2GB && CPU >= 2core && disk >= 30GB
  -- 集群机器可以通信
  -- 禁止swap分区
       swapoff -a

2. 二进制安装k8s
  -- 安装cfssl工具用于生成各种组件需要的证书.
     wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 && chmod +x cfssl_linux-amd64 && mv cfssl_linux-amd64 /usr/local/bin/cfssl
     wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 && chmod +x cfssljson_linux-amd64 && mv cfssljson_linux-amd64 /usr/local/bin/cfssljson
     wget https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 && chmod +x cfssl-certinfo_linux-amd64 && mv cfssl-certinfo_linux-amd64 /usr/local/bin/cfssl-certinfo
  -- 生成各种证书
  
  -- centos7系统初始化
     # 关闭防火墙和selinux
     systemctl stop firewalld && systemctl disable firewalld
     sed -i 's/enforcing/disabled/' /etc/selinx/config
     setenforce 0
    
     # 关闭swap
     swapoff -a 
     sed -ri 's/.*swap.*/#&' /etc/fstab

     # 根据实际情况设计主机名
     hostnamectl set-hostname <hostname>

     # 在master节点添加host映射信息
     cat >> /etc/hosts << EOF
     192.168.7.21  k8s-master
     192.168.7.22  k8s-node1
     192.168.7.23  k8s-node2
     EOF

     # 所有节点将ipv4添加流量桥接规则
     cat >/etc/sysctl.d/k8s.conf << EOF
     net.bridge.bridge-nf-call-ip6tables = 1
     net.brodge.bridge-nf-call-iptables = 1
     EOF
     sysctl --system

     yum install ntpdate -y && ntpdate time.windows.com

  -- etcd部署
     ...
  
  -- master节点部署
     ...

  -- node节点部署
     ...

  -- 一些插件部署
     ...

  
!