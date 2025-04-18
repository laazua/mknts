### 部署

##### 安装的k8sJiqian版本: v1.32.2
##### 所有节点OS均为: debian 12 bookworm
##### 所有节点的配置: 2核4G(或者更高配置)
##### 节点地址信息: master[node-00=192.168.165.80] worker[node-03=192.168.165.83,node-04192.168.165.84] lb[node-05=192.168.165.86]

- 说明(master&worker)
1. 节点环境初始化
2. 安装cri环境: containerd, runc
3. 直接下载二进制包: kubeadm、kubelet、kubectl 进行部署
4. 负载均衡安装(nginx或者haproxy + keepalived)

- 准备安装包
```bash
# lb 下载nginx
wget https://nginx.org/download/nginx-1.24.0.tar.gz
# cri 下载containerd
wget  https://github.com/containerd/containerd/releases/download/v2.0.0/containerd-2.0.0-linux-amd64.tar.gz
# k8s master&worker 下载二进制包
wget https://dl.k8s.io/v1.32.2/kubernetes-server-linux-amd64.tar.gz
# crictl
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.32.0/crictl-v1.32.0-linux-amd64.tar.gz
cat > /etc/crictl.yaml <<EOF
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 2
debug: true
EOF
```

- 负载均衡部署
```bash
# lb节点(192.168.165.86执行)
tar -xf nginx-1.24.0.tar.gz && cd nginx-1.24.0
sudo ./configure --prefix=/usr/local/nginx-1.24.0 --with-stream --without-http --without-http_uwsgi_module --without-http_scgi_module --without-http_fastcgi_module
sudo make && sudo make install
# 建立软连接方便更新
sudo ln -s /usr/local/nginx-1.24.0/sbin/nginx /usr/local/sbin/nginx
# 设置环境变量
echo 'export PATH=/usr/local/nginx/sbin:$PATH' >> /etc/profile.d/nginx.sh
# 加载环境变量
source /etc/profile.d/nginx.sh
# 修改nginx配置
cat > /usr/local/nginx-1.24.0/conf/nginx.conf <<EOF
worker_processes 1;
events {
    worker_connections  1024;
}
stream {
    upstream backend {
        least_conn;
        hash $remote_addr consistent;
        server 192.168.165.80:6443    max_fails=3 fail_timeout=30s;
    }
    server {
        listen 8443;
        proxy_connect_timeout 1s;
        proxy_pass backend;
    }
}
EOF
# 启动nginx
sudo nginx -t /usr/local/nginx/conf/nginx.conf
sudo nginx -c /usr/local/nginx/conf/nginx.conf

cat >> /etc/hosts <<EOF
192.168.165.80  node-00
192.168.165.83  node-03
192.168.165.84  node-04
192.168.165.86  lb.controller.plane.cn
EOF
```

- 部署流程
1. 节点初始化
```bash
# 安装ntpdate,iptables
sudo apt -y install ntpdate iptables
# 添加定时任务
crontab -e
# 添加如下内容
*/5 * * * * /usr/sbin/ntpdate ntp1.aliyun.com
# 启用 IPv4 数据包转发
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF
# 应用 sysctl 参数而不重新启动
sudo sysctl --system
# 配置hosts
cat >> /etc/hosts <<EOF
192.168.165.80  node-00
192.168.165.83  node-03
192.168.165.84  node-04
192.168.165.86  lb.controller.plane.cn
EOF
# 关闭swap
swapoff -a
sed -i 's/.*swap.*/#&/' /etc/fstab
```
2. 安装cri环境
```bash
# 安装runc
sudo install -m 755 runc.amd64 /usr/local/sbin/runc
# 添加containerd systemd服务配置
cat >/usr/lib/systemd/system/containerd.service <<EOF
[Unit]
Description=containerd container runtime
Documentation=https://containerd.io
After=network.target dbus.service

[Service]
Environment="HTTP_PROXY=http://192.168.165.89:8080"
Environment="HTTPS_PROXY=http://192.168.165.89:8080"
Environment="NO_PROXY=localhost,127.0.0.1"
ExecStartPre=-/sbin/modprobe overlay
ExecStart=/usr/local/bin/containerd

Type=notify
Delegate=yes
KillMode=process
Restart=always
RestartSec=5

# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNPROC=infinity
LimitCORE=infinity

# Comment TasksMax if your systemd version does not supports it.
# Only systemd 226 and above support this version.
TasksMax=infinity
OOMScoreAdjust=-999

[Install]
WantedBy=multi-user.targe
EOF

# 解压containerd
tar -xf containerd-2.0.0-linux-amd64.tar.gz && cd containerd-2.0.0-linux-amd64
# 配置containerd
sudo mkdir -p /etc/containerd
sudo containerd config default > /etc/containerd/config.toml
# 配置containerd cgroup驱动,如果默认是false改为true
# sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/g' /etc/containerd/config.toml
# 启动containerd
sudo systemctl daemon-reload
sudo systemctl enable --now containerd
# 查看containerd状态
sudo systemctl status containerd
```
3. 安装k8s
```bash
# 解压k8s二进制包
tar -xf kubernetes-server-linux-amd64.tar.gz && cd kubernetes/server/bin && cp kubeadm kubelet kubectl /usr/local/bin/
# 上传kubeadm、kubelet、kubectl到所有k8s节点
scp kubeadm kubelet kubectl 192.168.165.80:/usr/local/bin/
scp kubeadm kubelet kubectl 192.168.165.83:/usr/local/bin/
scp kubeadm kubelet kubectl 192.168.165.84:/usr/local/bin/
# 配置kubelet
cat > /usr/lib/systemd/system/kubelet.service <<EOF
[Unit]
Description=kubelet: The Kubernetes Node Agent
Documentation=https://kubernetes.io/docs/home/
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/kubelet \
  --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf \
  --kubeconfig=/etc/kubernetes/kubelet.conf \
  --pod-manifest-path=/etc/kubernetes/manifests \
  --config=/var/lib/kubelet/config.yaml
Restart=always
RestartSec=10
StartLimitInterval=0

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable kubelet

# 在其中一台master节点上执行(lb.controller.plane.cn为负载均衡的地址)
sudo kubeadm init \
  --control-plane-endpoint "lb.controller.plane.cn:8443" \
  --upload-certs \
  --pod-network-cidr=10.244.0.0/16 \
  --cri-socket unix:///run/containerd/containerd.sock \
  --image-repository registry.aliyuncs.com/google_containers

# 执行上面的的命令报错, 解决完报错，执行: kubeadm reset -f