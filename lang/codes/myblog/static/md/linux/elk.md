## 记一次elk技术栈部署过程(elasticsearch, filebeat, kibana)

* *注意事项*
* > 以上各个组件的版本都要选用一致(7.6.1)


* *elasticsearch部署*
```
  - 官网下载安装包,并修改配置
  - 主机添加elasticsearch启动es用户
  - 配置es用户的ulimit为4096(centos7修改/etc/security/limits.d/20-nproc.conf,添加一下内容)
    es    soft    nproc    4096
    es    hard    nproc    4096
    echo 'vm.max_map_count = 262144' >> /etc/sysctl.conf && sysctl -p (根据启动过程中报错更改vm.max_map_count的值)
  - 认证设置(在其中一个节点上运行如下命令)
    1.生成密钥: bin/elasticsearch-certutil ca  (根据提示继续，这里的提示中会让输入密码，在下面步骤5中要用到，最后会生成一个elastic-stack-ca.p12文件)
    2.生成证书: bin/elasticsearch-certutil cert -ca elastic-stack-ca.p12  (根据提示继续，会生成一个elastic-certificates.p12文件)
    3.将上面生成的文件拷贝到所有节点上的指定目录，并在配置文件中进行配置
    4.修改配置文件elasticsearch.yml
      http.cors.enabled: true
      http.cors.allow-origin: "*"
      http.cors.allow-headers: Authorization,X-Requested-With,Content-Type,Content-Length
      xpack.security.enabled: true
      xpack.security.authc.accept_default_password: true
      xpack.security.transport.ssl.enabled: true
      xpack.security.transport.ssl.verification_mode: certificate
      xpack.security.transport.ssl.keystore.path: #[es的安装路径]/config/certificates/elastic-certificates.p12
      xpack.security.transport.ssl.truststore.path: #[es的安装路径]/config/certificates/elastic-certificates.p12
    5.在每个节点上添加密码
      bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
      输入密码：与上面步骤1中的密码一致
    6.启动所有节点，在其中一个节点上设置集群登录认证密码：bin/elasticsearch-setup-passwords  interactive  (需要设置 elastic，apm_system，kibana，kibana_system，logstash_system，beats_system)
```

* *filebeat部署*
```
  - 从官网下载安装包并修改对应的配置
  - 使用普通用户启动filebeat
```
* *kibana部署*
```
  - 从官网下载安装包并修改对应的配置
  - 使用普通用户启动kibana
```
* *logstash*
```
  - 主要用作数据清洗，可根据实际情况部署
```
