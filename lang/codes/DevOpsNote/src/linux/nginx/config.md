# 配置

> 针对CPU的nginx配置优化  
> worker_processes 4;  
> worker_cpu_affinity 0001 0100 1000 0010;  

> 网络连接相关的配置  
> keepalive_timeout 60 50;  
> send_timeout 10s;  
> client_header_buffer_size 4K; # getconf PAGESIZE  
> multi_accept on;  

> 与事件驱动模型相关的配置  
> use epoll;  
> worker_connections 65535; # cat /proc/sys/fs/file-max  
> worker_rlimit_sigpending 1024;  
> devpoll_changes 64;  
> devpoll_events 64;  
> kqueue_changes 1024;  
> kqueue_events 1024;  
> epoll_changes 1024;  
> rtsig_signo signo;  
> rtsig_overflow_events 32;  
> rtsig_overflow_test 32;  
> rtsig_overflow_threshold 10;  

> ngx_http_gzip_module模块处理相关配置  
> gzip on;  
> gzip_buffers 32 4k | 16 8k;  
> gzip_comp_level 6; # 1-9  
> gzip_disable MSIE [4-6]\.; # 可以使用正在进行匹配  
> gzip_http_version 1.0|1.1;  
> gzip_min_length 1024;  
> gzip_proxied off | expired | no-cache | no-store | private | no_last_modified | no_etag | auth | any ...;  
> gzip_types text/plain application/x-javascript text/css application/xml;  
> gzip_vary on;  

> ngx_http_gzip_static_module模块相关配置  
> gzip_static on | off | always;  
> gzip_proxied expired no-cache no-store private auth;  

> ngx_http_gunzip_module模块相关配置
> gunzip_static on | off;
> gunzip_buffers 32 4k | 16 8k;  

> nginx后端服务器组相关配置  
> upstream backend {  
>   ip_hash; # keepalive connections | least_conn  
>   server test.com weight=3;  
>   server 127.0.0.1:8080 max_fails=3 fail_timeout=30s;  
>   server unix:/tmp/backend3;     
> }  

> 域名跳转  
> ...  
> server {  
>   listen 80;  
>   server_name jump.myweb.name;  
>   rewrite ^/ http://www.myweb.info/;  
>   ...    
> }  
> ...  
> server {  
>    listen 80;  
>    server_name jump.myweb.name jump.myweb.info;  
>    if ($host ~ myweb\.info) {  
>      rewrite ^(.*) http://jump.myweb.name$1 permanent;  
>    }  
> }  
> ...  
> server {  
>    listen 80;  
>    server_name jump1.myweb.name jump2.myweb.name;  
>    if ($http_host ~* ^(.*)\.myweb\.name$) {  
>      rewrite ^(.*) http://jump.myweb.name$1;  
>      break;    
>    }  
> }  
> ...  

> 域名镜像  
> ...  
> server {  
>    ...  
>    listen 80;  
>    server_name mirror1.myweb.name;  
>    rewrite ^(.*) http://jump1.myweb.name$1 last;  
> }  
> server {  
>   ...  
>   listen 81;
>   server_name mirror2.myweb.name;  
>   rewrite ^(.*) http://jump2.myweb.name$2 last;     
> }  

> 将某个子目录资源做镜像  
> server {  
>   listen 80;  
>   server_name jump.myweb.name;  
>   location ^~ /source1 {  
>     ...  
>     rewrite ^/source1(.*) http://jump.myweb.name/websrc2$1 last;  
>     break;   
>   }  
>   location ^~ /source2 {  
>     ...  
>     rewrite ^/source2(>*) http://jump.myweb.name/websrc2$1 last;  
>   }  
>   ...  
> }  

> 独立域名  
> server {  
>   ...  
>   listen 80;  
>   server_name bbs.myweb.name;  
>   rewrite ^(.*) http://www.myweb.name/bbs$1 last;  
>   break;  
> }  
> server {  
>   listen 81;  
>   server_name home.myweb.name;  
>   rewrite ^(.*) http://www.myweb.name/home$1 last;  
>   break;  
> }  

> 目录自动添加"/"  
> server {  
>   ...  
>   listen 81;  
>   server_name www.myweb.name;  
>   location ^~ /bbs {  
>     ...  
>     if (-d $request_filename) {  
>       rewrite ^/(.*)([^/])$ http://$host/$1$2/ permanent;  
>     }   
>   }  
> }  

> 合并目录  
> server {  
>   ...  
>   listen 80;  
>   server_name www.myweb.name;  
>   location ^~ /server {  
>     ...  
>     rewrite ^/server-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)\.htm$ /server/$1/$2/$3/$4/$5.html last;  
>     break;  
>   }    
> }  

> 防盗链  
> 根据文件类型实现防盗链  
> server {  
>   listen 80;  
>   server_name www.myweb.name;  
>   location ~* ^.+\.(gif|jpg|png|swf|flv|rar|zip)$ {  
>     ...  
>     valid_referers none blocked server_name *. myweb.name;  
>     if ($invalid_referer) {  
>       rewrite ^/ http://www.myweb.com/images/forbidden.png;  
>     } 
>   }
> }  
> 根据请求目录实现防盗链  
> server {  
>   ...  
>   listen 80;  
>   server_name www.myweb.name;  
>   location /file/ {  
>     ...  
>     root /server/file/;  
>     valid_referers none blocked server_name *. myweb.name;  
>     if ($invalid_referer) {  
>       rewrite ^/ http://www.myweb.com/images/forbidden.png;  
>     }  
>   }  
> } 