### ***tcp反向代理***

* *示例*
```
在stream{}中添加如下配置
stream {
  upstream backend {
    server backend1.example.com:12345;
    server backend2.example.com:12345;
    server backend3.example.com:12345;
  }

  server {
    listen 12345;
    proxy_pass backend;
  }
}
```