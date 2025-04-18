### kubeadm


- 部署 k8s 集群
1. 节点初始化
```bash
# 关闭交换分区
swapoff -a
# 永久关闭
vim /etc/fstab  # 注释掉 swap 分区
# 关闭防火墙（centos）
systemctl stop firewalld
systemctl disable firewalld
# 关闭 selinux
setenforce 0
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
# 内核参数优化
cat >> /etc/sysctl.d/k8s.conf <<EOF
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system
# ips模块安装
apt install -y ipvsadm ipset sysstat conntrack libseccomp2
# 配置ips模块
cat >> /etc/modules-load.d/ipvs.conf <<EOF
ip_vs
ip_vs_rr
ip_vs_wrr
ip_vs_sh
nf_conntrack
ip_tables
ip_set
xt_set
ipt_set
ipt_rpfilter
ipt_REJECT
ipip
EOF
# containerd 模块
cat >> /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF
# 加载模块
systemctl restart systemd-modules-load
```

2. 安装containerd
```bash
# 安装containerd
# containerd systemd服务配置
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

# 配置containerd 服务代理
mkdir -p /usr/lib/systemd/system/containerd.service.d
cat > /usr/lib/systemd/system/containerd.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://your.proxy.server:port"
Environment="HTTPS_PROXY=http://your.proxy.server:port"
Environment="NO_PROXY=localhost,127.0.0.1"
EOF

# 下载containerd安装包
wget https://github.com/containerd/containerd/releases/download/v2.0.0/containerd-2.0.0-linux-amd64.tar.gz
# 解压 containerd压缩包
tar -xvf containerd-2.0.0-linux-amd64.tar.gz -C /usr/local
# 下载cni插件
wget https://github.com/containernetworking/plugins/releases/download/v1.6.2/cni-plugins-linux-amd64-v1.6.2.tgz
# 解压 cni插件压缩包
mkdir -p /opt/cni/bin
tar -xvf cni-plugins-linux-amd64-v1.6.2.tgz -C /opt/cni/bin
# 下载 runc
wget https://github.com/opencontainers/runc/releases/download/v1.2.6/runc.amd64
# 安装runc
install -m 755 runc.amd64 /usr/local/sbin/runc
# 生成containerd配置文件
mkdir -p /etc/containerd
# 默认配置
# containerd config default > /etc/containerd/config.toml
cat >> /etc/containerd/config.toml <<EOF
version = 3
root = '/var/lib/containerd'
state = '/run/containerd'
temp = ''
plugin_dir = ''
disabled_plugins = []
required_plugins = []
oom_score = 0
imports = []

[grpc]
  address = '/run/containerd/containerd.sock'
  tcp_address = ''
  tcp_tls_ca = ''
  tcp_tls_cert = ''
  tcp_tls_key = ''
  uid = 0
  gid = 0
  max_recv_message_size = 16777216
  max_send_message_size = 16777216

[ttrpc]
  address = ''
  uid = 0
  gid = 0

[debug]
  address = ''
  uid = 0
  gid = 0
  level = ''
  format = ''

[metrics]
  address = ''
  grpc_histogram = false

[plugins]
  [plugins.'io.containerd.cri.v1.images']
    snapshotter = 'overlayfs'
    disable_snapshot_annotations = true
    discard_unpacked_layers = false
    max_concurrent_downloads = 3
    image_pull_progress_timeout = '5m0s'
    image_pull_with_sync_fs = false
    stats_collect_period = 10

    [plugins.'io.containerd.cri.v1.images'.pinned_images]
      sandbox = 'registry.k8s.io/pause:3.10'

    [plugins.'io.containerd.cri.v1.images'.registry]
      config_path = ''

    [plugins.'io.containerd.cri.v1.images'.image_decryption]
      key_model = 'node'

  [plugins.'io.containerd.cri.v1.runtime']
    enable_selinux = false
    selinux_category_range = 1024
    max_container_log_line_size = 16384
    disable_apparmor = false
    restrict_oom_score_adj = false
    disable_proc_mount = false
    unset_seccomp_profile = ''
    tolerate_missing_hugetlb_controller = true
    disable_hugetlb_controller = true
    device_ownership_from_security_context = false
    ignore_image_defined_volumes = false
    netns_mounts_under_state_dir = false
    enable_unprivileged_ports = true
    enable_unprivileged_icmp = true
    enable_cdi = true
    cdi_spec_dirs = ['/etc/cdi', '/var/run/cdi']
    drain_exec_sync_io_timeout = '0s'
    ignore_deprecation_warnings = []

    [plugins.'io.containerd.cri.v1.runtime'.containerd]
      default_runtime_name = 'runc'
      ignore_blockio_not_enabled_errors = false
      ignore_rdt_not_enabled_errors = false

      [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes]
        [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc]
          runtime_type = 'io.containerd.runc.v2'
          runtime_path = ''
          pod_annotations = []
          container_annotations = []
          privileged_without_host_devices = false
          privileged_without_host_devices_all_devices_allowed = false
          base_runtime_spec = ''
          cni_conf_dir = ''
          cni_max_conf_num = 0
          snapshotter = ''
          sandboxer = 'podsandbox'
          io_type = ''

          [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options]
            BinaryName = ''
            CriuImagePath = ''
            CriuWorkPath = ''
            IoGid = 0
            IoUid = 0
            NoNewKeyring = false
            Root = ''
            ShimCgroup = ''
            ## 新增配置
            SystemdCgroup = true

    [plugins.'io.containerd.cri.v1.runtime'.cni]
      bin_dir = '/opt/cni/bin'
      conf_dir = '/etc/cni/net.d'
      max_conf_num = 1
      setup_serially = false
      conf_template = ''
      ip_pref = ''
      use_internal_loopback = false

  [plugins.'io.containerd.gc.v1.scheduler']
    pause_threshold = 0.02
    deletion_threshold = 0
    mutation_threshold = 100
    schedule_delay = '0s'
    startup_delay = '100ms'

  [plugins.'io.containerd.grpc.v1.cri']
    disable_tcp_service = true
    stream_server_address = '127.0.0.1'
    stream_server_port = '0'
    stream_idle_timeout = '4h0m0s'
    enable_tls_streaming = false

    [plugins.'io.containerd.grpc.v1.cri'.x509_key_pair_streaming]
      tls_cert_file = ''
      tls_key_file = ''

  [plugins.'io.containerd.image-verifier.v1.bindir']
    bin_dir = '/opt/containerd/image-verifier/bin'
    max_verifiers = 10
    per_verifier_timeout = '10s'

  [plugins.'io.containerd.internal.v1.opt']
    path = '/opt/containerd'

  [plugins.'io.containerd.internal.v1.tracing']

  [plugins.'io.containerd.metadata.v1.bolt']
    content_sharing_policy = 'shared'

  [plugins.'io.containerd.monitor.container.v1.restart']
    interval = '10s'

  [plugins.'io.containerd.monitor.task.v1.cgroups']
    no_prometheus = false

  [plugins.'io.containerd.nri.v1.nri']
    disable = false
    socket_path = '/var/run/nri/nri.sock'
    plugin_path = '/opt/nri/plugins'
    plugin_config_path = '/etc/nri/conf.d'
    plugin_registration_timeout = '5s'
    plugin_request_timeout = '2s'
    disable_connections = false

  [plugins.'io.containerd.runtime.v2.task']
    platforms = ['linux/amd64']

  [plugins.'io.containerd.service.v1.diff-service']
    default = ['walking']
    sync_fs = false

  [plugins.'io.containerd.service.v1.tasks-service']
    blockio_config_file = ''
    rdt_config_file = ''

  [plugins.'io.containerd.shim.v1.manager']
    env = []

  [plugins.'io.containerd.snapshotter.v1.blockfile']
    root_path = ''
    scratch_file = ''
    fs_type = ''
    mount_options = []
    recreate_scratch = false

  [plugins.'io.containerd.snapshotter.v1.btrfs']
    root_path = ''

  [plugins.'io.containerd.snapshotter.v1.devmapper']
    root_path = ''
    pool_name = ''
    base_image_size = ''
    async_remove = false
    discard_blocks = false
    fs_type = ''
    fs_options = ''

  [plugins.'io.containerd.snapshotter.v1.native']
    root_path = ''

  [plugins.'io.containerd.snapshotter.v1.overlayfs']
    root_path = ''
    upperdir_label = false
    sync_remove = false
    slow_chown = false
    mount_options = []

  [plugins.'io.containerd.snapshotter.v1.zfs']
    root_path = ''

  [plugins.'io.containerd.tracing.processor.v1.otlp']

  [plugins.'io.containerd.transfer.v1.local']
    max_concurrent_downloads = 3
    max_concurrent_uploaded_layers = 3
    config_path = ''

[cgroup]
  path = ''

[timeouts]
  'io.containerd.timeout.bolt.open' = '0s'
  'io.containerd.timeout.metrics.shimstats' = '2s'
  'io.containerd.timeout.shim.cleanup' = '5s'
  'io.containerd.timeout.shim.load' = '5s'
  'io.containerd.timeout.shim.shutdown' = '3s'
  'io.containerd.timeout.task.state' = '2s'

[stream_processors]
  [stream_processors.'io.containerd.ocicrypt.decoder.v1.tar']
    accepts = ['application/vnd.oci.image.layer.v1.tar+encrypted']
    returns = 'application/vnd.oci.image.layer.v1.tar'
    path = 'ctd-decoder'
    args = ['--decryption-keys-path', '/etc/containerd/ocicrypt/keys']
    env = ['OCICRYPT_KEYPROVIDER_CONFIG=/etc/containerd/ocicrypt/ocicrypt_keyprovider.conf']

  [stream_processors.'io.containerd.ocicrypt.decoder.v1.tar.gzip']
    accepts = ['application/vnd.oci.image.layer.v1.tar+gzip+encrypted']
    returns = 'application/vnd.oci.image.layer.v1.tar+gzip'
    path = 'ctd-decoder'
    args = ['--decryption-keys-path', '/etc/containerd/ocicrypt/keys']
    env = ['OCICRYPT_KEYPROVIDER_CONFIG=/etc/containerd/ocicrypt/ocicrypt_keyprovider.conf']
EOF
```

3. 配置apt源
```bash
sudo apt install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/kubernetes.gpg
echo 'deb [trusted=yes] https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main' > /etc/apt/sources.list.d/kubernetes.list
# 如果apt update 报错：W: GPG error: https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B53DC80D13EDEF05, 则执行如下命令
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B53DC80D13EDEF05
gpg --export --armor B53DC80D13EDEF05 | tee /etc/apt/trusted.gpg.d/kubernetes.asc
# 再次执行：curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /etc/apt/trusted.gpg.d/kubernetes.asc
apt update

# 安装kubeadm、kubelet、kubectl
apt install -y kubeadm=1.26.0-00 kubelet=1.26.0-00 kubectl=1.26.0-00
# 锁定版本
apt-mark hold kubeadm=1.26.0-00 kubelet=1.26.0-00 kubectl=1.26.0-00
```

4. 初始化k8s集群
```bash
# 注意可以使用--config参数指定配置文件来自定义初始化集群参数
[--config定制组件](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
# master节点执行:
kubeadm init \
  --control-plane-endpoint "192.168.165.85:7443" \
  --upload-certs \
  --pod-network-cidr=10.244.0.0/16 \
  --cri-socket unix:///run/containerd/containerd.sock \
  --image-repository registry.aliyuncs.com/google_containers

# --control-plane-endpoint 控制面的IP地址和端口为负载均衡器的IP地址和端口(需要单独部署)
# 成功输出如下:
# Your Kubernetes control-plane has initialized successfully!

# To start using your cluster, you need to run the following as a regular user:

#   mkdir -p $HOME/.kube
#   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
#   sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Alternatively, if you are the root user, you can run:

#   export KUBECONFIG=/etc/kubernetes/admin.conf

# You should now deploy a pod network to the cluster.
# Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
#   https://kubernetes.io/docs/concepts/cluster-administration/addons/

# You can now join any number of the control-plane node running the following command on each as root:

#   kubeadm join 192.168.165.85:7443 --token u1xp42.jvv65cetgiuq6e9h \
# 	--discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c \
# 	--control-plane --certificate-key 3087bc5222acba4e0e864dcfc80e72808d706801c8bff26115dcba114bc470b6

# Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
# As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
# "kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

# Then you can join any number of worker nodes by running the following on each as root:

# kubeadm join 192.168.165.85:7443 --token u1xp42.jvv65cetgiuq6e9h \
# 	--discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chmod 600 ~/.kube/config
```

- 安装网络插件(三选一)
1. calico
```bash
# 安装calico网络插件
1. kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.2/manifests/tigera-operator.yaml
2. wget https://raw.githubusercontent.com/projectcalico/calico/v3.28.2/manifests/custom-resources.yaml -O calico.yaml
3. vim calico.yaml && 更改cidr网段为初始化参数--pod-network-cidr的网段(10.244.0.0/16)
4. kubectl apply -f calico.yaml
```
2. flannel

3. cilium
```bash
# 安装helm工具
# github直接下载helm工具
# 解压并拷贝到/usr/local/bin目录下

# cilium安装
helm repo add cilium https://helm.cilium.io
# 根据需要调整cilium/values.yaml文件中的配置
helm install  cilium ./cilium/ -n kube-system
```

- 如果后续还想加入节点
```bash
########## 加入master节点:
# 获取集群证书密钥
sudo kubeadm init phase upload-certs --upload-certs
# 获取加入master节点需要执行的命令: 这里的certificate-key是上面获取的证书密钥
kubeadm token create --print-join-command --certificate-key <certificate-key>
# 上面执行的命令输出如下:
# kubeadm join 192.168.165.85:7443 --token czqvwv.rmhezi9p3zcs37cl --discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c --control-plane --certificate-key cefbf02ec98ea9faf777981a614f23d0ea3091889fdcb1d55d5c2feee178c1c6
# 在需要加入的master节点上执行上面的输出:
kubeadm join 192.168.165.85:7443 --token czqvwv.rmhezi9p3zcs37cl --discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c --control-plane --certificate-key cefbf02ec98ea9faf777981a614f23d0ea3091889fdcb1d55d5c2feee178c1c6

########### 加入worker节点:
# 在已有的控制平面执行以下命令，获取加入worker节点需要执行的命令: 
kubeadm token create --print-join-command
# 上面执行的命令输出如下:
# kubeadm join 192.168.165.85:7443 --token cpp4mg.8a8ziftp499hmr4a --discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c
# 在需要加入的worker节点上执行上面的输出:
kubeadm join 192.168.165.85:7443 --token cpp4mg.8a8ziftp499hmr4a --discovery-token-ca-cert-hash sha256:f5ff06a1705a95dce227b702ded23d579407421dbbc071d085e5ca8e40deca4c
```

- 节点role标签重置
```bash
# 重置node节点role标签(worker)
# kubectl label node <node-name> node-role.kubernetes.io/worker=
kubectl label node node-03 node-role.kubernetes.io/worker=
# 重置node节点role标签(master)
# kubectl label node <node-name> node-role.kubernetes.io/master=
kubectl label node node-01 node-role.kubernetes.io/master=
```