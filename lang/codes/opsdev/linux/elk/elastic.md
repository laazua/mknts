### elasticsearch

#### 部署
- **下载elasticsearch-8.17.3-linux-x86_64.tar.gz**
1. wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.17.3-linux-x86_64.tar.gz
2. mkdir /data/ && tar -xf elasticsearch-8.17.3-linux-x86_64.tar.gz -C /data/

- **节点环境初始化**
1. 新建elasticsearch启动用户: groupadd elastic && useradd  -g elastic elastic -s /sbin/nologin  
   或者：sudo adduser --system --group --no-create-home elastic
2. vim /etc/security/limits.conf
```text
elastic soft nofile 65535
elastic hard nofile 65535
```
3. 禁用交换分区: swapoff -a (临时) && vim /etc/fstab (永久: 注释掉swap行)
4. 设置虚拟内存限制: echo "vm.max_map_count=262144" >>/etc/sysctl.conf && sysctl -p

- **ca证书**
1. bin/elasticsearch-certutil ca
2. bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12
3. mkdir config/certs && mv *.p12 config/certs/

- **http证书**
1. bin/elasticsearch-certutil http
```text
## Elasticsearch HTTP Certificate Utility

The 'http' command guides you through the process of generating certificates
for use on the HTTP (Rest) interface for Elasticsearch.

This tool will ask you a number of questions in order to generate the right
set of files for your needs.

## Do you wish to generate a Certificate Signing Request (CSR)?

A CSR is used when you want your certificate to be created by an existing
Certificate Authority (CA) that you do not control (that is, you don't have
access to the keys for that CA). 

If you are in a corporate environment with a central security team, then you
may have an existing Corporate CA that can generate your certificate for you.
Infrastructure within your organisation may already be configured to trust this
CA, so it may be easier for clients to connect to Elasticsearch if you use a
CSR and send that request to the team that controls your CA.

If you choose not to generate a CSR, this tool will generate a new certificate
for you. That certificate will be signed by a CA under your control. This is a
quick and easy way to secure your cluster with TLS, but you will need to
configure all your clients to trust that custom CA.

Generate a CSR? [y/N]n

## Do you have an existing Certificate Authority (CA) key-pair that you wish to use to sign your certificate?

If you have an existing CA certificate and key, then you can use that CA to
sign your new http certificate. This allows you to use the same CA across
multiple Elasticsearch clusters which can make it easier to configure clients,
and may be easier for you to manage.

If you do not have an existing CA, one will be generated for you.

Use an existing CA? [y/N]y

## What is the path to your CA?

Please enter the full pathname to the Certificate Authority that you wish to
use for signing your new http certificate. This can be in PKCS#12 (.p12), JKS
(.jks) or PEM (.crt, .key, .pem) format.
CA Path: /data/elasticsearch-8.17.3/config/certs/elastic-stack-ca.p12
Reading a PKCS12 keystore requires a password.
It is possible for the keystore's password to be blank,
in which case you can simply press <ENTER> at the prompt
Password for elastic-stack-ca.p12:

## How long should your certificates be valid?

Every certificate has an expiry date. When the expiry date is reached clients
will stop trusting your certificate and TLS connections will fail.

Best practice suggests that you should either:
(a) set this to a short duration (90 - 120 days) and have automatic processes
to generate a new certificate before the old one expires, or
(b) set it to a longer duration (3 - 5 years) and then perform a manual update
a few months before it expires.

You may enter the validity period in years (e.g. 3Y), months (e.g. 18M), or days (e.g. 90D)

For how long should your certificate be valid? [5y] 50y

## Do you wish to generate one certificate per node?

If you have multiple nodes in your cluster, then you may choose to generate a
separate certificate for each of these nodes. Each certificate will have its
own private key, and will be issued for a specific hostname or IP address.

Alternatively, you may wish to generate a single certificate that is valid
across all the hostnames or addresses in your cluster.

If all of your nodes will be accessed through a single domain
(e.g. node01.es.example.com, node02.es.example.com, etc) then you may find it
simpler to generate one certificate with a wildcard hostname (*.es.example.com)
and use that across all of your nodes.

However, if you do not have a common domain name, and you expect to add
additional nodes to your cluster in the future, then you should generate a
certificate per node so that you can more easily generate new certificates when
you provision new nodes.

Generate a certificate per node? [y/N]n

## Which hostnames will be used to connect to your nodes?

These hostnames will be added as "DNS" names in the "Subject Alternative Name"
(SAN) field in your certificate.

You should list every hostname and variant that people will use to connect to
your cluster over http.
Do not list IP addresses here, you will be asked to enter them later.

If you wish to use a wildcard certificate (for example *.es.example.com) you
can enter that here.

Enter all the hostnames that you need, one per line.
When you are done, press <ENTER> once more to move on to the next step.


You did not enter any hostnames.
Clients are likely to encounter TLS hostname verification errors if they
connect to your cluster using a DNS name.

Is this correct [Y/n]y

## Which IP addresses will be used to connect to your nodes?

If your clients will ever connect to your nodes by numeric IP address, then you
can list these as valid IP "Subject Alternative Name" (SAN) fields in your
certificate.

If you do not have fixed IP addresses, or not wish to support direct IP access
to your cluster then you can just press <ENTER> to skip this step.

Enter all the IP addresses that you need, one per line.
When you are done, press <ENTER> once more to move on to the next step.

192.168.165.86
192.168.165.87

You entered the following IP addresses.

 - 192.168.165.86
 - 192.168.165.87

Is this correct [Y/n]y

## Other certificate options

The generated certificate will have the following additional configuration
values. These values have been selected based on a combination of the
information you have provided above and secure defaults. You should not need to
change these values unless you have specific requirements.

Key Name: elasticsearch
Subject DN: CN=elasticsearch
Key Size: 2048

Do you wish to change any of these options? [y/N]n

## What password do you want for your private key(s)?

Your private key(s) will be stored in a PKCS#12 keystore file named "http.p12".
This type of keystore is always password protected, but it is possible to use a
blank password.

If you wish to use a blank password, simply press <enter> at the prompt below.
Provide a password for the "http.p12" file:  [<ENTER> for none]

## Where should we save the generated files?

A number of files will be generated including your private key(s),
public certificate(s), and sample configuration options for Elastic Stack products.

These files will be included in a single zip archive.

What filename should be used for the output zip file? [/data/elasticsearch-8.17.3/elasticsearch-ssl-http.zip] 

Zip file written to /data/elasticsearch-8.17.3/elasticsearch-ssl-http.zip
```
2. unzip elasticsearch-ssl-http.zip && cp elasticsearch/http.p12 config/certs/
3. cd config/ && tar -czf certs.tar.gz   # 这里打包的证书可以给其他节点使用

- **elasticsearch.yml**
1. 修改elsasticsearch.yml配置
```yaml
cluster.name: EsCluster
node.name: node-1
path.data: /data/elasticsearch-8.17.3/data
path.logs: /data/elasticsearch-8.17.3/logs
network.host: 192.168.165.86
http.port: 9000
discovery.seed_hosts: ["192.168.165.86", "192.168.165.87"]
cluster.initial_master_nodes: ["node-1", "node-2"]

xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.client_authentication: required
xpack.security.transport.ssl.keystore.path: /data/elasticsearch-8.17.3/config/certs/elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: /data/elasticsearch-8.17.3/config/certs/elastic-certificates.p12

xpack.security.http.ssl.enabled: true  # 配置http证书后可以使用https访问,测试可以设置为false
xpack.security.http.ssl.keystore.path: /data/elasticsearch-8.17.3/config/certs/http.p12
```
2. chown -R elastic:elastic /data/elasticsearch-8.17.3/

- **elasticsearch.service**
1. vim /usr/lib/systemd/system/elasticsearch.service
```text
[Unit]
Description=Elasticsearch
Documentation=https://www.elastic.co
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=elastic
Group=elastic
ExecStart=/data/elasticsearch-8.17.3/bin/elasticsearch
Restart=on-failure
LimitNOFILE=65536
LimitNPROC=4096
TimeoutStopSec=600
LimitMEMLOCK=infinity

[Install]
WantedBy=multi-user.target
```
2. systemctl daemon-reload && systemctl enable elasticsearch && systemctl start elasticsearch
3. 设置默认账户密码：sudo bin/elasticsearch-setup-passwords interactive
4. 重置用户elastic密码：sudo bin/elasticsearch-reset-password -u elastic

- **部署说明**
1. [以上部署参考官网](https://www.elastic.co/guide/en/elasticsearch/reference/current/bootstrap-checks-xpack.html)
2. 上面的证书生成只需要一个节点上执行即可, 其他节点上只需要拷贝证书即可.
3. 使用chrome插件：Elasticsearch Multi-head 查看集群状态