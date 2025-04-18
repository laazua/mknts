# 安装 kubernetes

---

- [二进制安装 kubernetes 集群](https://github.com/confucuis/bin-install-k8s.git)
- [二级制安装 kubernetes 集群参考](https://github.com/cby-chen/Kubernetes/blob/main/doc/v1.27.1-CentOS-binary-install-IPv6-IPv4-Three-Masters-Two-Slaves-Offline.md)
- [kubernetes 集群中安装 ingress-nginx](./yaml/ingress-nginx-deploy.yaml)

---

- 安装 ingress-nginx

```
  1. 安装ingress-nginx官网helm包进行操作(把相关的镜像手动导入到k8s.io这个namespace中)
```

- 存储卷安装

```
  1. 参照官网进行安装(主要注意nfs服务的主目录权限)
```
