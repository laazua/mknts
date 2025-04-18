##### 蓝绿发布

```
  - kubectl get all
  - kubectl apply -f .
  - kubectl describe svc service-name
  - kubectl delete po --all
  - kubectl delete svc --all

  要切换版本更改svn-example.yml中的version字段,将其指定为pod对应的yml文件中对应的版本
  然后重新发布
```