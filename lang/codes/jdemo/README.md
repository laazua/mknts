### jdemo

* *环境*
1. [mave](https://maven.apache.org/download.cgi)
2. [jdk21.0.3](https://www.oracle.com/java/technologies/downloads/#java21)

* *使用*
1. 初始化项目: mvn archetype:generate -DgroupId=com.example -DartifactId=jdemo -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
2. 打包项目: cd jdemo && mvn package
3. 运行jar包: java -jar target\jdemo-1.0-SNAPSHOT.jar

* *资料*
1. [java21](https://docs.oracle.com/en/java/javase/21/index.html)