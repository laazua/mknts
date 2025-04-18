#### deployment

* **deployment**
```
  - 滚动发布抽象
  - 滚动发布操作: 修改deployment的yml文件中image字段中对应镜像的版本, 然后再次发布
```

* **操作**
```
  - kubectl get all
  - kubectl apply -f .
  - kubectl rollout history name
  - kubectl rollout undo name
  - kubectl delete deploy name
```