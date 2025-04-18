#### pvc&&pv

```
  - 解耦k8s数据存储

kubectl apply -f local-pv.yml
kubectl apply -f mysql-pvc.yml
kubectl apply -f mysql-svc.yml
kubectl apply -f petclinic-svc.yml
```