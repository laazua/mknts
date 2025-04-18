# kubernetes应用
---

* **部署**    
  kubectl apply -f nginx-demo  

* *注意*  
  nginx-demo路径下包含: deployment.yaml,service.yaml,ingress.yaml 
  deployment.yaml中的spec.template.spec.containers[].ports[].containerPort对应pod中应用的启动端口    
  service.yaml中的spec.ports[].targetPort端口对应deployment.yaml中的spec.template.spec.containers[].ports[].containerPort端口    
  ingress.yaml中的spec.rules[].http.paths[].backend.service.port.number端口对应service.yaml中的spec.ports[].port端口
  ingress.yaml中的域名要与访问域名一致
* 检查流量是否能正常进入应用:    
  1. service层流量检查    
  kubectl get svc -n default    
  curl ip:8888    

  2. ingress层流量检查    
  kubectl get ing -n default    
  curl -H "host:demo-nginx-example.com" 10.20.158.92:80    