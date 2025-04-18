### eBPF

---

**eBPF 编程**  
使用[libbpf-bootstrap](https://github.com/libbpf/libbpf-bootstrap)脚手架:
克隆 libbpf-bootstrap 脚手架  
git clone https://github.com/libbpf/libbpf-bootstrap  
更新 libbpf-bootstrap 的子模块  
cd libbpf-bootstrap && git submodule update --init --recursive  
在 examples 对应的语言下编写代码  
c 规范: app.bpf.c 内核空间文件命名, app.c 用户空间文件命名
在 Makefile 的 APPS 中添加应用 app 名称

---

[eunomia ebpf](https://eunomia.dev/)  
[ebpf 内核文档](https://prototype-kernel.readthedocs.io/en/latest/bpf/)
