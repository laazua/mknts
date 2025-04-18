#!/bin/bash

# centos 7

function k8s_env() {
    # 关闭防火墙
    systemctl disable --now firewalld
    
    # 基础软件
    yum install wget expect vim net-tools ntp bash-completion ipvsadm ipset jq iptables conntrack sysstat libseccomp -y

    # 关闭selinx
    sed -i 's#enforcing#disabled#g' /etc/sysconfig/selinux

    # k8s集群关闭swap
    swapoff -a
    sed -i.bak 's/^.*centos-swap/#&/g' /etc/fstab
    echo 'KUBELET_EXTRA_ARGS="--fail-swap-on=false"' > /etc/sysconfig/kubelet

    # 配置yun源
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
    curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
    curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

    # 刷新缓存
    yum makecache

    # 更新系统
    yum update -y --exclud=kernel*
    https://linux.cc.iitk.ac.in/mirror/centos/elrepo/kernel/el7/x86_64/RPMS/kernel-lt-devel-4.4.245-1.el7.elrepo.x86_64.rpm
    https://linux.cc.iitk.ac.in/mirror/centos/elrepo/kernel/el7/x86_64/RPMS/kernel-lt-4.4.245-1.el7.elrepo.x86_64.rpm
    # 升级内核
    yum localinstall -y kernel-lt*
    grub2-set-default  0 && grub2-mkconfig -o /etc/grub2.cfg
    grubby --default-kernel

    # 安装ipvs
    yum install -y conntrack-tools ipvsadm ipset conntrack libseccomp
    
    # 加载IPVS模块
    cat > /etc/sysconfig/modules/ipvs.modules <<EOF
    #!/bin/bash
    ipvs_modules="ip_vs ip_vs_lc ip_vs_wlc ip_vs_rr ip_vs_wrr ip_vs_lblc ip_vs_lblcr ip_vs_dh ip_vs_sh ip_vs_fo ip_vs_nq ip_vs_sed ip_vs_ftp nf_conntrack"
    for kernel_module in \${ipvs_modules}; do
        /sbin/modinfo -F filename \${kernel_module} > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            /sbin/modprobe \${kernel_module}
        fi
    done
EOF
    chmod 755 /etc/sysconfig/modules/ipvs.modules && bash /etc/sysconfig/modules/ipvs.modules && lsmod | grep ip_vs
  
    # 内核参数优化
    cat > /etc/sysctl.d/k8s.conf << EOF
    net.ipv4.ip_forward = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    fs.may_detach_mounts = 1
    vm.overcommit_memory=1
    vm.panic_on_oom=0
    fs.inotify.max_user_watches=89100
    fs.file-max=52706963
    fs.nr_open=52706963
    net.ipv4.tcp_keepalive_time = 600
    net.ipv4.tcp.keepaliv.probes = 3
    net.ipv4.tcp_keepalive_intvl = 15
    net.ipv4.tcp.max_tw_buckets = 36000
    net.ipv4.tcp_tw_reuse = 1
    net.ipv4.tcp.max_orphans = 327680
    net.ipv4.tcp_orphan_retries = 3
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_max_syn_backlog = 16384
    net.ipv4.ip_conntrack_max = 65536
    net.ipv4.tcp_max_syn_backlog = 16384
    net.ipv4.top_timestamps = 0
    net.core.somaxconn = 16384
EOF
    systcl --system

    # 时间同步
    yum install ntp -y
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    echo 'Asia/Shanghai' > /etc/timezone
    ntpdate time2.aliyun.com

    # 写入定时任务
    echo "*/1 * * * * ntpdate time2.aliyun.com > /dev/null 2>&1" >> /var/spool/cron/root

    # 安装cfssl工具用于生成各种组件需要的证书(运维服安装或者master安装,主要是在哪个节点上操作.).
    # wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 && chmod +x cfssl_linux-amd64 && mv cfssl_linux-amd64 /usr/local/bin/cfssl
    # wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 && chmod +x cfssljson_linux-amd64 && mv cfssljson_linux-amd64 /usr/local/bin/cfssljson
    # wget https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 && chmod +x cfssl-certinfo_linux-amd64 && mv cfssl-certinfo_linux-amd64 /usr/local/bin/cfssl-certinfo
}

function docker_install() {
    # 安装docker
    yum install -y yum-utils device-mapper-persistent-data lvm2
    yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

    yum install docker-ce -y

    systemctl daemon-reload
    systemctl restart docker
    systemctl enable --now docker.service
}

function main() {
    k8s_env
    docker_install
}

main "$@"
