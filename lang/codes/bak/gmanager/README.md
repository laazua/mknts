### gmanager

* *描述*
```
  - gmanager是一个游戏多区服管理工具
  - 技术栈: fastapi + grpc
```

* *部署*
```
  - 使用pdm工具进行项目依赖管理
  - 分别将gmaster和gservant的源码部署到运维服和游戏服
  - 分别进入程序gmaster和程序gservant根目录,运行: pdm install
  - 生成认证文件分别拷贝至gmaster/cert目录下和gservant/cert目录下
  - 使用manage.sh脚本管理gmaster和gservant的启停:
    bash manage.sh [start|stop|check]
```

<!-- 
- 如果在pyproject.toml文件中定义了[tool.pdm.scripts], 则:
  pdm run start => 启动应用
  pdm run stop  => 关闭应用
  pdm run check => 检查应用
 -->

<!-- 
openssl genrsa -out ca.key 
openssl req -new -x509 -days 36500 -key ca.key -out ca.crt -config certificate.conf 
openssl genrsa -out server.key 
openssl req -new -key server.key -out server.csr -config certificate.conf
openssl req -newkey rsa:1024 -key server.key -out server.csr -config certificate.conf
openssl x509 -req -days 36500 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt

=====================================================================================================
openssl genrsa -passout pass:1234 -des3 -out ca.key 4096
openssl req -passin pass:1234 -new -x509 -days 36500 -key ca.key -out ca.crt -subj  "/C=SP/ST=Italy/L=Ornavasso/O=Test/OU=Test/CN=Root CA"

openssl genrsa -passout pass:1234 -des3 -out server.key 4096
openssl genrsa -passout pass:1234 -des3 -out client.key 4096

openssl req -passin pass:1234 -new -key server.key -out server.csr -subj  "/C=SP/ST=Italy/L=Ornavasso/O=Test/OU=Server/CN=sample.com"
openssl req -passin pass:1234 -new -key client.key -out client.csr -subj  "/C=SP/ST=Italy/L=Ornavasso/O=Test/OU=Client/CN=localhost"

openssl x509 -req -passin pass:1234 -days 36500 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt
openssl x509 -req -passin pass:1234 -days 36500 -in client.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out client.crt

openssl rsa -passin pass:1234 -in server.key -out server.key
openssl rsa -passin pass:1234 -in client.key -out client.key
 -->