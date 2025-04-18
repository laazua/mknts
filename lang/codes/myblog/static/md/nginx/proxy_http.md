#### ***http反向代理***

* *示例*
```
在http{}中添加如下配置:
server {
  listen 80;
  server_name example.com;

  location / {
    proxy_pass http://localhost:8080;
  }
}
```