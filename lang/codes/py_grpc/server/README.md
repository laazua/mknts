### server

* *描述*
```
  - 分别进入server和client目录下生成对应的grpc代码(示例如下):
    ../../.venv/bin/python  -m grpc_tools.protoc -I ../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto
  - 修改grpc文件helloworld_pb2_grpc.py导报代码: 
    import helloworld_pb2 as helloworld__pb2
    from . import helloworld_pb2 as helloworld__pb2
```
* *生成证书*
  - [参考](https://blog.csdn.net/cowbin2012/article/details/100134114)
```
    - cp /etc/ssl/openssl.cnf ./cert

    - 生成根证书:
      openssl genrsa -out ca.key 2048
      openssl req -new -key ca.key -out ca.csr
      echo "subjectAltName=DNS:test.grpc.com,IP:127.0.0.1" > cert_extensions (根据时间情况修改域名和IP)
      openssl x509 -req -days 36500 -in ca.csr -signkey ca.key -extfile cert_extensions -out ca.crt

    - 生成服务器端证书:
      openssl genrsa -out server.key 2048
      openssl req -new -key server.key -out server.csr(根据提示天入对应字段,Common Name为/etc/hosts文件下ip对应的域名)
      openssl ca -in server.csr -out server.crt -extfile cert_extensions -cert ca.crt -keyfile ca.key
      (上面这一步报错,按提示新建对饮目录: mkdir demoCA/newcerts && touch demoCA/index.txt && echo 01 > demoCA/serial)

    - 生成客户端证书:
      openssl genrsa -out client.key 2048
      openssl req -new -key client.key -out client.csr(根据提示天入对应字段,Common Name为/etc/hosts文件下ip对应的域名)
      openssl ca -in client.csr -out client.crt -cert ca.crt -keyfile ca.key
      (上面一步报错,则修改demoCA/index.txt.attr文件中字段unique_subject为no)
      
    - 因为server端是多节点模式,所以在生成证书过程中需要注意:
      1. ca证书的域名填写与client端证书的域名填写保持一致
      2. server端证书根据不同节点填写不同的域名,并将此域名与节点IP填写到节点主机的/etc/hosts中
      3. 在生成server端证书时,不同节点的域名与IP对应情况需要根据实际情况对cert/cert_extensions文件中的域名与IP进行修改
      4. 所有server端节点证书和clent端证书都使用相同的ca证书生成
      5. 在生成.csr证书文件的过程中需要输入值的字段:
         Country Name (2 letter code) [AU]:      # 国家
         State or Province Name (full name) [Some-State]:     #省份
         Locality Name (eg, city) []:    # 城市
         Common Name (e.g. server FQDN or YOUR name) []:    # 域名
```
