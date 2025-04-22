# 灰度发布

* *负载均衡(根据weight导流)*  

配置  
```
upstream demo {
    server 192.168.165.81:8885 weight=1;
    server 192.168.165.82:8885 weight=5;
    server 192.168.165.83:8885 weight=5;
}

server {
    listen 80;
    server_name demo-test.com;
    location / {
        proxy_pass http://demo;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

发布过程  
  1) upstream demo服务器中部署的是业务服务  
  2) 在未更新业务服务的代码时,流量是均匀(调整weight权重都相等)分布到三台业务服务器上  
  3) 先更新一台(81)服务的代码,调整weight权重为1:5:5,将少量流量分布到已更新的服务器(81)上; 重启nginx(nginx -s reload)  
  4) 验证已更新业务服务器(81)是否有问题,如果没问题调整三台weight权重比例相等(恢复流量均匀分布到三台主机上); 重启nginx  

* *负载均衡(客户端特定cookie参数导流)*  

配置  
```
upstream demo {
    #server 192.168.165.81:8885;
    server 192.168.165.82:8885;
    server 192.168.165.83:8885;
}

upstream test {
    server 192.168.165.81:8885;
}

server {
    listen 80;
    server_name demo-test.com;

    # 设置back_host变量
    set $back_host "demo";
    # 判断cookie中srv_host变量的值
    if ($cookie_srv_host = "test") {
        set $back_host $cookie_srv_host;
    }
    location / {
	    proxy_pass http://$back_host;
    }
}
```

发布过程  
  1) upstream demo服务器中部署的业务服务  
  2) 当客户端访问携带cookie(srv_host=test)时: curl -b 'srv_host=test' http://demo-test.com  
     流量都导入到upstream test服务器上(已经更新了业务代码), 测试无误后将所有业务服务的代码都更新  
  3) 将upstream test中的服务器移动到upstream demo中, 重启服务器  
