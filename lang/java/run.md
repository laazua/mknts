### 运行jar

- **说明**
  > java项目pom.xml中未指定入口类，则使用一下命令运行jar包:  
  > java -cp|-classpath|--class-path app.jar package.MainClass  
  > 其中-cp,-classpath,--class-path 三个参数同义,选用一种即可  
  > 方式一:  java -cp app.jar com.example.app.MainClass  
  > 方式二:  java -classpath app.jar com.example.app.MainClass  
  > 方式三:  java --class-path app.jar com.example.app.MainClass  

- **注意: 开发打包的java版本必须与真实运行环境中的java版本一致**


- **例如如下项目**
```bash
## 项目结构
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
