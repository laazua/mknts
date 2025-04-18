# kustomize 工具部署 k8s 应用

- _描述_  
  用于部署 k8s 原生 yaml 资源对象

- _安装_

  1. 原生 kustomize 工具
  2. kubectl kustomize 子命令 [参考](https://kustomize.io/)

- _目录结构_

  someApp/  
  ├── base  
  │   ├── deployment.yaml  
  │   ├── env.txt  
  │   ├── ingress.yaml  
  │   ├── kustomization.yaml  
  │   └── service.yaml  
  └── overlays  
  ├── dev  
  │   ├── kustomization.yaml  
  │   └── patch.yaml  
  └── pro  
  ├── deployment.yaml  
  ├── kustomization.yaml  
  └── patch.yaml

* _示例_  
  在 overlays/pro 目录下执行:  
  kustomize edit set replicas nginx-deployment=5|kustomize build

- [参考官方文档](https://kubectl.docs.kubernetes.io/zh/)
- [参考官方仓库](https://github.com/kubernetes-sigs/kustomize)
