### gmms

* **游戏运维管理**
  * *基于fastapi, rpyc, vue-admin*
  * *功能*
```
      1. 创建项目
      2. 开服
      3. 区服[启动|关闭|更新]
      4. 用户日志记录
      ...
```

* **api**
  * ![Image text](/imgs/api.png)

![Image text](/imgs/login.png)    
![Image text](/imgs/22.png)
![Image text](/imgs/log.png)
![Image text](/imgs/open.png)
![Image text](/imgs/svn.png)
![Image text](/imgs/open.png)
![Image text](/imgs/zone.png)

* **生成证书**
  * *生成私钥.key*
    * openssl genrsa -out ca.key 2048
  * *生成.csr*
    * req -new -key ca.key -out ca.csr
  * *生成ca根证书(.crt或者.cert)*
    * openssl x509 -req -days 3650 -in ca.csr -signkey ca.key -out ca.cert
  * [参考](https://blog.csdn.net/liuchunming033/article/details/48470575)

* *注*
  * 代码虽然写得很烂,但是该实现的功能都能用.
