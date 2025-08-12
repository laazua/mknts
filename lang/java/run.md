### 运行jar

- java -cp app.jar package.MainClass
- java -classpath app.jar package.MainClass
- 示例
```text
如果我的项目的包是: com.laazua.app, 则运行命令:
java -classpath app.jar com.laazua.app.App
```

- 注意: 开发打包的java版本必须与真实运行环境中的java版本一致

- 运行jar包
```bash
## 格式: java -cp app.jar  com.example.app.App

##### 例如如下项目
jspi/
├── pom.xml
├── README.md
└── src
    ├── main
    │   ├── java
    │   │   └── com
    │   │       └── laazua
    │   │           └── jspi
    │   │               ├── ConsoleLog.java
    │   │               ├── FileLog.java
    │   │               ├── JspiApplication.java
    │   │               └── Logger.java
    │   └── resources
    │       ├── application.properties
    │       └── META-INF
    │           └── services
    │               └── com.laazua.jspi.Logger
    └── test
        └── java
            └── com
                └── laazua
                    └── jspi
                        └── JspiApplicationTests.java
## 打包: mvn package -Dmaven.test.skip=true
## 部署jspi-0.0.1-SNAPSHOT.jar 包,执行: java -cp jspi-0.0.1-SNAPSHOT.jar com.laazua.jspi.JspiApplication
```
