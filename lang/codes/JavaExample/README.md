### JavaExample

这是关于Java学习的示例代码仓库, Java版本: jdk-23.0.2

- **学习**  
1. [教程](https://dev.java/)  
2. [指导](https://docs.oracle.com/en/java/javase/23/)  
3. [文档](https://docs.oracle.com/en/java/index.html)
4. [三方包](https://mvnrepository.com/)

- **打包:**
1. mvn clean package
2. mvn clean package -DskipTests
3. mvn clean package -Dmaven.test.skip=true

- **运行**
1. java -jar JavaExample-1.0-SNAPSHOT.jar

- **jdk生成jre**  
1. 列出可以添加的模块: java --list-modules
2. 生成jre: jlink --module-path $JAVA_HOME/jmods --add-modules java.base,java.sql --output jre 

- **jpackage打包**
1. 方式一:  
   a. jlink --module-path $JAVA_HOME/jmods --add-modules java.base --output JavaExample/runtime  
   b. jpackage --name JavaExample --input target --main-jar JavaExample-1.0-SNAPSHOT.jar --main-class org.example.Main --type app-image --dest JavaExample --runtime-image JavaExample/runtime  

2. 方式二:  
   a. jpackage --name JavaExample --input target --main-jar JavaExample-1.0-SNAPSHOT.jar --module-path $JAVA_HOME/jmods --add-modules java.base --jlink-options --bind-services -d JavaExample --type app-image  
