### k8s

* **k8s架构**
  * *master节点*
  ```
    - kube-apiserver
    - kube-scheduler
    - controller-manager
    - etcd
  ```
  * *node节点*
  ```
    - kubelet
    - kube-proxy
    - container runtime
    - 插件(addons)
    - ...
  ```

* **发布资源**
  * kubectl apply -f test.yml
  * kubectl apply -f dirname

* **k8s资源对象**
  * *Service*
    * *蓝绿发布*
    <!-- ![alt text](img/service-blue-green-deployment.png) -->
    * *NodePort*
    <!-- ![alt text](imgs/nodePort-service.png) -->
    * *ClusterIP*
    <!-- ![alt text](imgs/service-clusterIp.png) -->
    * *LoadBalancer*
  * *Pod*
    <!-- ![alt text](imgs/pod.png) -->
  * *ReplicaSet*
    <!-- ![alt text](imgs/replicaset.png) -->
  * *Deployment*
  * *Namespace*
    <!-- ![alt text](imgs/namespace.png) -->
  * *ConfigMap*
    <!-- ![alt text](imgs/configmap.png) -->
  * *Secret*
    <!-- ![alt text](imgs/secret.png) -->
  
  * *ReplicationController*
  * *HorizontalPodAutoscaler*
  * *StatefulSet*
  * *PersistentVolume*
