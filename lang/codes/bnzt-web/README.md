#### bnzt-web

* **部署**
```
  - 修改vue.config.js中的publicPath的值为: './'
  - 修改rouuter/index.js中的createRouter函数中的mode为: 'hash'
  - 打包:
    npm run build:prod
  - 部署到服务器的/var/www/html目录下
```

* **nginx配置**
```
server {
    listen  8886;
    location /bnzt {
        root  /var/www/html;
        index  index.html;
        try_files $uri $uri/ /index.html;
        add_header Access-Control-Allow-Methods "*";
        add_header Access-Control-Allow-Headers "*";
        autoindex  on;
        autoindex_exact_size  on;
        autoindex_localtime  on;
    }
    location ~*/api/ {
      proxy_pass http://127.0.0.1:8888;
    }
    error_page 404 /404.html;
    location = /404.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}

```